import logging

import os
import mimetypes

from django.http import StreamingHttpResponse, HttpResponseNotAllowed
from django.views.generic.base import View

from rest_framework.permissions import IsAuthenticated

from DiplomaQ.vars import USER_ROLES

from users.models import User, CuratorStudent
from core.models import DiplomaFile

logger = logging.getLogger('DiplomaQ')


class IsCuratorPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLES[1][0]

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, DiplomaFile):
            return CuratorStudent.objects.filter(curator=request.user, id=obj.user_link_id).exists()
        return super(IsCuratorPermission, self).has_object_permission(request, view, obj)


class IsStudentPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.role == USER_ROLES[0][0]

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, DiplomaFile):
            return CuratorStudent.objects.filter(student=request.user, id=obj.user_link_id).exists()
        return super(IsStudentPermission, self).has_object_permission(request, view, obj)


class StreamingResponseView(View):
    file_name = None
    http_method = 'get'

    def get_generator(self):
        raise NotImplementedError('The method is not implemented')

    def get_filename(self):
        return self.file_name

    def __get_response(self, *args, **kwargs):
        self.__is_not_used(*args, **kwargs)

        try:
            generator = self.get_generator()
        except Exception as e:
            logger.exception(e)
            raise
        if generator is None:
            raise RuntimeError()

        file_name = getattr(generator, 'name', None) or self.get_filename()
        if not isinstance(file_name, str) or len(file_name) == 0:
            raise RuntimeError()

        file_size = getattr(generator, 'size', None)

        mimetype = mimetypes.guess_type(os.path.basename(file_name))[0]
        response = StreamingHttpResponse(generator, content_type=mimetype)
        if file_size is not None:
            response['Content-Length'] = file_size
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
        return response

    def get(self, *args, **kwargs):
        if self.http_method != 'get':
            return HttpResponseNotAllowed(['get'])
        return self.__get_response(*args, **kwargs)

    def post(self, *args, **kwargs):
        if self.http_method != 'post':
            return HttpResponseNotAllowed(['post'])
        return self.__get_response(*args, **kwargs)

    def __is_not_used(self, *args, **kwargs):
        pass
