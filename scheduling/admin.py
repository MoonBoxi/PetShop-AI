from django.contrib import admin
from .models import ServiceType, Service, TimeSlot, Booking

admin.site.register(ServiceType)
admin.site.register(Service)
admin.site.register(TimeSlot)
admin.site.register(Booking)