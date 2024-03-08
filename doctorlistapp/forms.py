from django.forms import ModelForm
from .models import Doctor


class DoctorForm (ModelForm):
    class Meta:
        model = Doctor
        fields = [
            "f_name",
            "l_name",
            "hospital",
            "practice",
            "years_of_experience",
        ]
