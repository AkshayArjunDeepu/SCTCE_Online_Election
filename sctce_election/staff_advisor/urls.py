from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_adv_home),
    path('add_student/', views.student_details),
    path('login/', views.staff_adv_login),
    path('generate_otp/', views.generate_otp)
]
