from django.contrib import admin
from .models import Elevator
# Register your models here.
class ElevatorAdmin(admin.ModelAdmin):
    list_display = ('id','status','destinations','direction','door')
    
admin.site.register(Elevator, ElevatorAdmin)