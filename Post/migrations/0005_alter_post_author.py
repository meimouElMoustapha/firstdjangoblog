# Generated by Django 3.2.7 on 2021-09-16 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_alter_userprofile_user'),
        ('Post', '0004_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Profile.userprofile'),
            preserve_default=False,
        ),
    ]