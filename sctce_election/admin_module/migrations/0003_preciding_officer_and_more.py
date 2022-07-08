# Generated by Django 4.0.6 on 2022-07-08 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0002_rename_create_election_upcoming_election'),
    ]

    operations = [
        migrations.CreateModel(
            name='preciding_officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20)),
                ('election_id', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'other')], max_length=1)),
            ],
        ),
        migrations.RenameField(
            model_name='upcoming_election',
            old_name='name',
            new_name='election_name',
        ),
    ]
