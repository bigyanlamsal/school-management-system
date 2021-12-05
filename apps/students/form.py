from django import forms
from .models import Notice_info, Vacancy_info

class NoticesForm(forms.ModelForm):
    class Meta:
        model = Notice_info
        fields= ['title', 'detail', 'passport', 'date']

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy_info
        fields= ['subject', 'level', 'image_vacancy', 'date', 'end_date']