# Generated by Django 3.2 on 2022-06-11 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_alter_user_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, to='club.Group'),
        ),
    ]
