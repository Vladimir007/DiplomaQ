from django.core.management.base import BaseCommand

from DiplomaQ.vars import USER_ROLES
from users.models import User


class Command(BaseCommand):
    help = """
Used to create users for testing purposes. Be ware: all users will be deleted before.
Username for students is "studentX" where X is integer 1..(number of students).
Username for curators is "curatorX" where X is integer 1..(number of curators).
Administrator username is "admin". All users will be created with the same password.
"""
    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add_argument(
            '--students', dest='students', type=int, default=10,
            help='Number of students to populate. Default value is 10.'
        )
        parser.add_argument(
            '--curators', dest='curators', type=int, default=3,
            help='Number of curators to populate. Default value is 3.'
        )
        parser.add_argument(
            '--password', dest='password', type=str, default="password123",
            help='Password for all users. Default value is "password123".'
        )

    def handle(self, *args, **options):
        User.objects.all().delete()

        objects_list = []

        # Students
        for i in range(1, options['students'] + 1):
            user = User(
                username='student{}'.format(i),
                first_name='Firstname{}'.format(i),
                last_name='Lastname{}'.format(i),
                is_active=True
            )
            user.set_password(options['password'])
            objects_list.append(user)

        # Curators
        for i in range(1, options['curators'] + 1):
            user = User(
                username='curator{}'.format(i),
                first_name='Name{}'.format(i),
                last_name='Lastname{}'.format(i),
                is_active=True,
                role=USER_ROLES[1][0]
            )
            user.set_password(options['password'])
            objects_list.append(user)

        # Admin
        user = User(
            username='admin', first_name='Firstname', last_name='Lastname',
            is_active=True, is_staff=True, is_superuser=True, role=USER_ROLES[1][0]
        )
        user.set_password(options['password'])
        objects_list.append(user)

        User.objects.bulk_create(objects_list)

        if options['verbosity'] >= 1:
            self.stdout.write("Users were successfully populated.")
