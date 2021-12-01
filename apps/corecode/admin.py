from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.AcademicSession)
admin.site.register(models.AcademicTerm)
admin.site.register(models.Subject)
admin.site.register(models.StudentClass)
