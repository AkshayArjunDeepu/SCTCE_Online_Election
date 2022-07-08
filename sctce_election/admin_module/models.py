from math import degrees
from django.db import models

# Create your models here.

class upcoming_election(models.Model):
    election_id   = models.CharField(max_length = 10 )
    election_name = models.CharField(max_length = 50)
    fname_officer = models.CharField(max_length = 50)
    lname_officer = models.CharField(max_length = 50)
    election_date = models.DateField()

    def __str__(self):
        return self.name + ' ('+ self.id + ')'
    
class election_history(models.Model):
    election_id       = models.CharField(max_length = 30)
    name              = models.CharField(max_length = 50)
    date              = models.DateField()
    fname_principal   = models.CharField(max_length = 50)
    lname_principal   = models.CharField(max_length = 50)
    result            = models.CharField(max_length = 50)

    def __str__(self):
        return self.name + ' ('+ self.date + ')'

class preciding_officer(models.Model):
    
    gender_choices = (
        ('M', 'male'),
        ('F', 'female'),
        ('O', 'other')
    )

    employee_id = models.CharField(max_length = 20)
    #election_id = models.ForeignKey(upcoming_election.election_id, on_delete = models.CASCADE)
    election_id = models.CharField(max_length = 20)
    first_name  = models.CharField(max_length = 30)
    last_name   = models.CharField(max_length = 30)
    gender      = models.CharField(max_length = 1, choices = gender_choices)

    def __str__(self):
        return self.first_name + self.last_name + ' ('+ self.employee_id+') '


class candidate(models.Model):
    first_name  = models.CharField(max_length = 30)
    last_name   = models.CharField(max_length = 30)
    adm_no      = models.IntegerField()
    apply_position   = models.CharField(max_length = 30)
    position_id      = models.CharField(max_length = 10)

    def __str__(self):
        return self.first_name +' ('+self.apply_position+ ')'

class polling_station(models.Model):
    station_id = models.CharField(max_length = 20)
    class_no   = models.IntegerField()
    floor_no   = models.IntegerField()
    preciding_officer = models.CharField(max_length = 30)
    n_nodes = models.IntegerField(null = True)

    def __str__(self):
        return 'class no:' +str(self.class_no) + ' ('+str(self.floor_no)+') '



class current_election_detail(models.Model):
    election_name        = models.CharField(max_length = 30)
    election_id          = models.CharField(max_length = 30)
    active_poll_stations = models.IntegerField()
    total_students       = models.IntegerField()
    students_voted       = models.IntegerField()
    students_pending     = models.IntegerField()
    polling_percentage   = models.FloatField()

    def __str__(self):
        return self.election_name+' ('+self.electon_id+')'

class election_posts(models.Model):

    depts_choices = (
        ('CS', 'Computer Science'),
        ('EC', 'Electronics and Communications'),
        ('BT', 'Biotechnology'),
        ('ME', 'Mechanical'),
        ('P', 'Production'),
        ('All', 'All')
    )

    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('All', 'All')
    )

    year_choices = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
        ('All', 'All')
    )

    degree_choices = (
        ('M', 'Mtech'),
        ('B', 'Btech'),
        ('All', 'All')
    )

    post_id = models.CharField(max_length = 30)
    position_name = models.CharField(max_length = 30)
    depts = models.CharField(max_length = 30, choices = depts_choices)
    gender  = models.CharField(max_length = 30, choices = gender_choices)
    year  = models.CharField(max_length = 30, choices = year_choices)
    degree = models.CharField(max_length = 30, choices = degree_choices)

    def __str__(self):
        return self.position_name


