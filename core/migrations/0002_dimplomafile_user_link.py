# Generated by Django 2.2.7 on 2019-11-25 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dimplomafile',
            name='user_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='users.CuratorStudent'),
        ),
    ]
