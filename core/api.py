from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from DiplomaQ.utils import IsCuratorPermission, IsStudentPermission
from core.models import DiplomaFile

from core.serializers import DiplomaSerializer, CommentSerializer


class UploadFileView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = DiplomaFile.objects
    serializer_class = DiplomaSerializer


class ChangeCommentView(RetrieveUpdateAPIView):
    permission_classes = (IsCuratorPermission,)
    queryset = DiplomaFile.objects
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'diploma_id'


class RemoveDiplomaFileView(DestroyAPIView):
    permission_classes = (IsStudentPermission,)
    queryset = DiplomaFile.objects
    lookup_url_kwarg = 'diploma_id'
