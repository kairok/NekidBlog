# Generated by Django 2.1.4 on 2018-12-10 09:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20181208_1802'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='UserSigned',
        ),
        migrations.AlterModelOptions(
            name='usersigned',
            options={'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
    ]
