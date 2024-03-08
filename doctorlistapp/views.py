from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor
from .forms import DoctorForm


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


def create_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(False)
            doctor.save()
            return redirect("get_all_doctors")
    else:
        form = DoctorForm()

    context = {
        "doctor_form": form,
    }
    return render(request, "doctor_form.html", context)


def edit_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("get_all_doctors")

    else:
        form = DoctorForm(instance=doctor)
    context = {
        "doctor_object": doctor,
        "doctor_form": form,
    }
    return render(request, "edit_doctor.html", context)


def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        doctor.delete()
        return redirect("get_all_doctors")
    return render(request, "delete.html")
