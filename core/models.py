from django.db import models
from users.models import User, CuratorStudent


class DiplomaFile(models.Model):
    user_link = models.ForeignKey(CuratorStudent, models.CASCADE, related_name='files')
    file = models.FileField(upload_to='diplomas')
    name = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(default='', blank=True)

    class Meta:
        db_table = 'diploma_files'
