# Generated by Django 3.2.6 on 2021-09-06 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='deactivated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
