from DiplomaQ.vars import USER_ROLES
from users.models import User


def fill_users():
    User.objects.all().delete()

    objects_list = []

    # Create students
    for i in range(1, 11):
        user = User(
            username='student{}'.format(i),
            first_name='Firstname{}'.format(i),
            last_name='Lastname{}'.format(i),
            is_active=True
        )
        user.set_password('password123')
        objects_list.append(user)

    # Create curators
    for i in range(1, 4):
        user = User(
            username='curator{}'.format(i),
            first_name='Name{}'.format(i),
            last_name='Lastname{}'.format(i),
            is_active=True,
            role=USER_ROLES[1][0]
        )
        user.set_password('password123')
        objects_list.append(user)

    # Create admin
    user = User(
        username='admin', first_name='Firstname', last_name='Lastname',
        is_active=True, is_staff=True, is_superuser=True, role=USER_ROLES[1][0]
    )
    user.set_password('password123')
    objects_list.append(user)

    User.objects.bulk_create(objects_list)
