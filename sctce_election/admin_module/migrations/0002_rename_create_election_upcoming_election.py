# Generated by Django 4.0.6 on 2022-07-08 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='create_election',
            new_name='upcoming_election',
        ),
    ]
