# Generated by Django 4.0.6 on 2022-07-08 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0003_preciding_officer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='polling_station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(max_length=20)),
                ('class_no', models.IntegerField()),
                ('floor_no', models.IntegerField()),
                ('preciding_officer', models.CharField(max_length=30)),
            ],
        ),
    ]
