from django.forms import ModelForm
from .models import Doctor


class DoctorForm (ModelForm):
    class Meta:
        model = Doctor
        fields = [
            "first_name",
            "last_name",
            "hospital",
            "practice",
            "years_of_experience",
            "doctor_url",
            "doctor_img_url",
        ]
# class SearchForm(Form):
