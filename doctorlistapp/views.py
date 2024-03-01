from django.shortcuts import render, get_object_or_404
from .models import Doctor


def get_all_doctors(request):
    doctors = Doctor.objects.all()
    all_doctors_template = "all_doctors.html"
    context = {
        "doctors": doctors
    }
    return render(request, all_doctors_template, context)


def get_doctor_by_id(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    context = {
        "doctor": doctor,
    }
    return render(request, "doctor_detail.html", context)
