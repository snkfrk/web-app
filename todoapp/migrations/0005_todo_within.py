# Generated by Django 4.2.4 on 2023-08-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_alter_todo_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='within',
            field=models.BooleanField(default=False),
        ),
    ]
