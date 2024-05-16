from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor
from .forms import DoctorForm


def get_all_doctors(request):

    search_term = request.GET.get('search')
    if search_term:
        doctors = Doctor.objects.filter(tags__icontains=search_term, status=True)
    else:
        doctors = Doctor.objects.filter(status=True)
    all_doctors_template = "home.html"
    context = {
        "doctors": doctors
    }
    return render(request, all_doctors_template, context)


def get_pending_doctors(request):

    doctors = Doctor.objects.filter(status=False)
    pending_doctors_template = "pending.html"
    context = {
        "doctors": doctors
    }
    return render(request, pending_doctors_template, context)


def search_doctors(request, search_term):
    doctors = Doctor.objects.filter(tags__icontains=search_term)

    search_result_template = "search_result.html"
    context = {
        "doctors": doctors
    }
    return render(request, search_result_template, context)


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
