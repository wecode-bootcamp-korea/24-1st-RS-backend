# Generated by Django 3.2.6 on 2021-09-07 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_deactivated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='deactivated_at',
        ),
    ]
