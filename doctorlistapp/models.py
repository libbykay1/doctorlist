from django.db import models


class Doctor(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    practice = models.CharField(max_length=50)
    doctor_url = models.URLField()
    years_of_experience = models.SmallIntegerField(blank=True)
