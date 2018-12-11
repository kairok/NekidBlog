# Generated by Django 2.1.4 on 2018-12-11 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_auto_20181211_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signed',
            name='_to',
        ),
        migrations.RemoveField(
            model_name='signed',
            name='_who',
        ),
        migrations.AddField(
            model_name='signed',
            name='to',
            field=models.ManyToManyField(related_name='to_who', to=settings.AUTH_USER_MODEL, verbose_name='Авторы'),
        ),
        migrations.AddField(
            model_name='signed',
            name='who',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='from_who', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
