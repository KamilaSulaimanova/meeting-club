# Generated by Django 3.2 on 2022-06-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
        migrations.AlterField(
            model_name='group',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]