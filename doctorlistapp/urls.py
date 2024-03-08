from django.urls import path
from .views import (
    get_all_doctors,
    get_doctor_by_id,
    create_doctor,
    edit_doctor
)

urlpatterns = [
    path("doctors", get_all_doctors, name="get_all_doctors"),
    path("doctors/<int:id>", get_doctor_by_id, name="get_doctor_by_id"),
    path("doctors/new", create_doctor, name="create_doctor"),
    path("doctors/edit/<int:id>", edit_doctor, name="get_doctor_by_id"),
]
