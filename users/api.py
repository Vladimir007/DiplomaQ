from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response

from DiplomaQ.vars import USER_ROLES
from DiplomaQ.utils import IsCuratorPermission

from users.models import User, CuratorStudent
from users.serializers import StudentListSerializer, NewStudentSerializer


class GetAvailableUsers(GenericAPIView):
    permission_classes = (IsCuratorPermission,)
    serializer_class = StudentListSerializer

    def get_queryset(self):
        return User.objects.filter(my_curator=None, role=USER_ROLES[0][0]).order_by('last_name', 'first_name')

    def filter_queryset(self, queryset):
        query_value = self.request.query_params.get('query')
        if not query_value:
            return queryset
        query_value = query_value.split()
        if len(query_value) == 2:
            return queryset.filter(last_name__iexact=query_value[0], first_name__istartswith=query_value[1])
        return queryset.filter(last_name__istartswith=query_value[0])

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'results': serializer.data})


class NewStudentAPIView(CreateAPIView):
    permission_classes = (IsCuratorPermission,)
    serializer_class = NewStudentSerializer
    queryset = CuratorStudent.objects
