from django.contrib import admin
from .models import Property, Booking, Review, Payment


# Register your models here.
admin.site.register(Property)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Payment)

