from django.contrib import admin
from .models import Load

class LoadAdmin(admin.ModelAdmin):
    list_display = ("origin", "destination", "email", "phone_number", "total_km", "rate")

admin.site.register(Load, LoadAdmin)

