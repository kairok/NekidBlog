# Generated by Django 2.1.4 on 2018-12-11 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20181211_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='user',
            new_name='blog',
        ),
    ]