from django.contrib import admin
from .models import Contact,Doctor, Patient, Appointment
# Register your models here.

admin.site.register(Contact)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)