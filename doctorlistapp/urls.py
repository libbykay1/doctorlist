from django.urls import path
from .views import (
    get_all_doctors,
    get_doctor_by_id,
    create_doctor,
    edit_doctor,
    search_doctors,
    get_pending_doctors
)

urlpatterns = [
    path("doctors", get_all_doctors, name="get_all_doctors"),
    path("pending/doctors/<int:id>", get_doctor_by_id, name="get_doctor_by_id"),
    path("doctors/new", create_doctor, name="create_doctor"),
    path("doctors/edit/<int:id>", edit_doctor, name="get_doctor_by_id"),
    path("doctors/<str:search_term>", search_doctors, name="search_doctors"),
    path("pending/doctors", get_pending_doctors, name="get_pending_doctor"),
]
