# Generated by Django 4.2.6 on 2023-10-09 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='created',
            new_name='create',
        ),
    ]
