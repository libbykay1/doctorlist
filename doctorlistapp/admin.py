from django.contrib import admin

from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
	list_display = (
		"id",
        "first_name",
	    "last_name",
		"hospital",
		"practice",
		"years_of_experience",

	)
