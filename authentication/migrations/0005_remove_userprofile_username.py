# Generated by Django 5.1.1 on 2024-10-27 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_rename_full_name_userprofile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]