from django.db import models


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    practice = models.CharField(max_length=50)
    doctor_url = models.URLField()
    doctor_img_url = models.URLField(null=True, default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png")
    years_of_experience = models.PositiveIntegerField(blank=True)
    tags = models.TextField(null=True)
    status = models.BooleanField(null=True, default=False)

    def approve_doctor(self):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        self.hospital = self.hospital.capitalize()
        self.tags = f"{self.first_name}, {self.last_name}, {self.hospital}, {self.practice}"
        self.status = True
        self.save()
