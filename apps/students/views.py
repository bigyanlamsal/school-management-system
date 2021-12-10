import csv
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from apps.finance.models import Invoice

from .models import Student, StudentBulkUpload, Notice_info
from basic.models import Admission_Student

from .form import NoticesForm, VacancyForm
from django.shortcuts import render, redirect

class AdmissionListView(LoginRequiredMixin, ListView):
    context_object_name = 'obj'
    model = Admission_Student
    template_name = "students/admission_list.html"


class StudentListView(LoginRequiredMixin, ListView):
    context_object_name = 'obj'
    model = Student
    template_name = "students/student_list.html"

class AdmissionDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "students/admission_detail.html"

    def get_context_data(self, **kwargs):
        context = super(AdmissionDetailView, self).get_context_data(**kwargs)
        
        return context

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "students/student_detail.html"

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context["payments"] = Invoice.objects.filter(student=self.object)
        return context


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student
    fields = "__all__"
    success_message = "New student successfully added."

    def get_form(self):
        """add date picker in forms"""
        form = super(StudentCreateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        return form


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    fields = "__all__"
    success_message = "Record successfully updated."

    def get_form(self):
        """add date picker in forms"""
        form = super(StudentUpdateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["date_of_admission"].widget = widgets.DateInput(
            attrs={"type": "date"}
        )
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        # form.fields['passport'].widget = widgets.FileInput()
        return form


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("student-list")

class AdmissionDeleteView(LoginRequiredMixin, DeleteView):
    model = Admission_Student
    success_url = reverse_lazy("admission-list")


class StudentBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentBulkUpload
    template_name = "students/students_upload.html"
    fields = ["csv_file"]
    success_url = "/student/list"
    success_message = "Successfully uploaded students"


class DownloadCSVViewdownloadcsv(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="student_template.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "registration_number",
                "surname",
                "firstname",
                "other_names",
                "gender",
                "parent_number",
                "address",
                "current_class",
            ]
        )

        return response

def show_notice(request):
    form = NoticesForm()
    return render(request, 'students/notice_publish.html', {'form': form})

def show_vacancy(request):
    form = VacancyForm()
    return render(request, 'students/vacancy_publish.html', {'form': form})


def get_notice(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_data = NoticesForm(request.POST, request.FILES)
        # check whether it's valid:
        if form_data.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form_data.save()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NoticesForm()
    return redirect(show_notice)

def get_vacancy(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_data = VacancyForm(request.POST, request.FILES)
        # check whether it's valid:
        if form_data.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            success_message = "New vacancy successfully added"
            form_data.save()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = VacancyForm()
    return redirect(show_vacancy)