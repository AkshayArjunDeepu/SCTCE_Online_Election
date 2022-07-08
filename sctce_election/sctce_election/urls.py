
from django.contrib import admin
from django.urls import path, include


from django.http import HttpResponse
def welcome(request):
    return HttpResponse('<br><br><br><br><center><h1>Welcome To SCTCE Online Election Portal</h1></center>')


urlpatterns = [
    path('', welcome),
    path('admin/', admin.site.urls),
    path('staff_advisor/', include('staff_advisor.urls'))
]
