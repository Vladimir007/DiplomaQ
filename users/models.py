from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token

from DiplomaQ.vars import USER_ROLES


class User(AbstractUser):
    role = models.CharField(verbose_name=_('Role'), max_length=1, choices=USER_ROLES, default=USER_ROLES[0][0])
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def get_full_name(self):
        """
        Return the last_name plus the first_name, with a space in between.
        """
        full_name = '%s %s' % (self.last_name, self.first_name)
        return full_name.strip()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        db_table = 'users'


class CuratorStudent(models.Model):
    student = models.OneToOneField(User, models.CASCADE, related_name='my_curator')
    curator = models.ForeignKey(User, models.CASCADE, related_name='students')

    class Meta:
        db_table = 'curator_students'
