# Generated by Django 3.2 on 2022-06-11 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20220611_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
