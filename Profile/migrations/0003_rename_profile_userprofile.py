# Generated by Django 3.2.7 on 2021-09-16 13:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profile', '0002_auto_20210916_1119'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='userprofile',
        ),
    ]
