from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse

# Create your models here.

class Admission_Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    father_name  = models.CharField(max_length=50)
    mothers_name  = models.CharField(max_length=50)
    class_numbers = models.IntegerField(blank=True)

    phone_regex = RegexValidator(regex=r'^\+?977?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(validators=[phone_regex], max_length=13, blank=True) # validators should be a list

    email = models.EmailField(max_length=250)
    grade_value  = models.FloatField(max_length=3, blank=True)
    review  = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse("admission-detail", kwargs={"pk": self.pk})