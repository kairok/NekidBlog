# Generated by Django 2.1.4 on 2018-12-10 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181210_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersigned',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
