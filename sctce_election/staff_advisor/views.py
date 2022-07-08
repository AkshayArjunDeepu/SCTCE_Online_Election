from django.shortcuts import render
from django.http import HttpResponse

from .models import student_detail
from admin_module.models import preciding_officer
# Create your views here.

import math   #for generating otp
import random #for generating otp

def staff_adv_home(request):
    return HttpResponse('<h1>Welcome to the home page of staff advisor</h1>')

def student_details(request):

    if request.method == 'POST':
        current_student = student_detail(
            name        = request.POST['name'],
            roll_no     = request.POST['roll_no'],
            adm_no      = request.POST['adm_no'],
            department  = request.POST['department'],
            year        = request.POST['year'],
            gender      = request.POST['gender']
        )

        current_student.save()
        
        context = {
            'student_entered' : True,
            'student_name'    : request.POST['name']
        }

        return render(request, 'staff_adv_get_student.html', {'context' :context})


    #return HttpResponse('Student Successfully Added')
    context = {
        'student_entered' : False
    }
    return render(request, 'staff_adv_get_student.html', {'context': context})


def staff_adv_login(request):

    context = {
        'success' : False 
    }

    if request.method == 'POST':
        curr_staff_adv = preciding_officer(
            employee_id = request.POST['employee_id'],
            election_id = request.POST['election_id'],
            first_name  = request.POST['first_name'],
            last_name   = request.POST['last_name'],
            gender      = request.POST['gender']
        )

        curr_staff_adv.save()
        
        return HttpResponse('Preciding Officer / Staff Advisor has been added...')
        
    
    else:
        return render(request, 'staff_adv_login.html')

def generate_otp(request):
 
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return HttpResponse('Newly generated One Time Password (OTP): '+OTP)
        