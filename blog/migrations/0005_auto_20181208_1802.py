# Generated by Django 2.1.4 on 2018-12-08 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20181208_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Readspost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Прочитал',
                'verbose_name_plural': 'Прочитал',
            },
        ),
        migrations.RemoveField(
            model_name='clients',
            name='user',
        ),
        migrations.RemoveField(
            model_name='news',
            name='isreaded',
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
        migrations.AddField(
            model_name='readspost',
            name='new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.News', verbose_name='News'),
        ),
        migrations.AddField(
            model_name='readspost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]