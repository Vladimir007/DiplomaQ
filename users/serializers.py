from rest_framework import fields, serializers

from users.models import User, CuratorStudent


class StudentListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    value = fields.IntegerField(source='id')

    def get_name(self, instance):
        return '{} {}'.format(instance.last_name, instance.first_name)

    class Meta:
        model = User
        fields = ('name', 'value')


class NewStudentSerializer(serializers.ModelSerializer):
    curator = fields.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CuratorStudent
        fields = ('curator', 'student')
