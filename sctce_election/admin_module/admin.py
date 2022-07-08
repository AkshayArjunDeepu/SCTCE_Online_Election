from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.upcoming_election)
admin.site.register(models.election_history)
admin.site.register(models.preciding_officer)
admin.site.register(models.candidate)
admin.site.register(models.election_posts)
admin.site.register(models.polling_station)
admin.site.register(models.current_election_detail)
