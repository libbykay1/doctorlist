# Generated by Django 4.0.6 on 2024-05-02 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorlistapp', '0004_doctor_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
