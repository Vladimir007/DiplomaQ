from rest_framework import fields, serializers

from core.models import DiplomaFile


class DiplomaSerializer(serializers.ModelSerializer):
    comment = fields.CharField(required=False, allow_blank=True)

    def validate(self, attrs):
        data = super(DiplomaSerializer, self).validate(attrs)
        data['name'] = data['file'].name
        print(data.get('comment', 'NULL'))
        return data

    class Meta:
        model = DiplomaFile
        fields = ('file', 'comment', 'user_link')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiplomaFile
        fields = ('comment',)
