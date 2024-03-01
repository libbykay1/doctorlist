from django.urls import path
from .views import get_all_doctors,get_doctor_by_id

urlpatterns = [
    path("doctors", get_all_doctors, name="get_all_doctors"),
    path("doctors/<int:id>", get_doctor_by_id, name="get_doctor_by_id"),
]
