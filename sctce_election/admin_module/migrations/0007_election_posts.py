# Generated by Django 4.0.6 on 2022-07-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0006_candidate'),
    ]

    operations = [
        migrations.CreateModel(
            name='election_posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=30)),
                ('position_name', models.CharField(max_length=30)),
                ('depts', models.CharField(choices=[('CS', 'Computer Science'), ('EC', 'Electronics and Communications'), ('BT', 'Biotechnology'), ('ME', 'Mechanical'), ('P', 'Production')], max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=30)),
                ('year', models.CharField(choices=[('1', 'First Year'), ('2', 'Second Year'), ('3', 'Third Year'), ('4', 'Fourth Year')], max_length=30)),
                ('degree', models.CharField(choices=[('M', 'Mtech'), ('B', 'Btech')], max_length=30)),
            ],
        ),
    ]