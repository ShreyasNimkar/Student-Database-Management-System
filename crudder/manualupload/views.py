from urllib import response
from django.shortcuts import render
from manualupload import forms
from .models import Student
from .resources import StudentResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FormName
# Create your views here.


def index(request):
    return render(request, 'index.html')


def form_name_view(request):
    form_class = FormName
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            student = Student(
                name=form.cleaned_data['name'], email=form.cleaned_data['email'], grade=form.cleaned_data['grade'],
                rollno=form.cleaned_data['rollno'], division=form.cleaned_data['division'], mobno=form.cleaned_data['mobno'])
            student.save()

    students = Student.objects.all()
    return render(request, 'manualupload/formpage.html', {'form': form, 'students': students})


def viewform(request):
    students = Student.objects.all()
    return render(request, 'manualupload/viewform.html', {'students': students})


def excel_upload_view(request):
    if request.method == 'POST':
        student_resource = StudentResource()
        dataset = Dataset()
        new_student = request.FILES['myfile']

        if not new_student.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'manualupload/excelpage.html')

        imported_data = dataset.load(new_student.read(), format='xlsx')
        for data in imported_data:
            value = Student(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
            )
            value.save()
    return render(request, 'manualupload/excelpage.html')


def getStudent(request, rollno):
    student = Student(rollno=rollno)


def getStudents(request, rollno):
    student = Student(rollno=rollno)


def deleteData(request, id):
    if request.method == "POST":
        pi = Student.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/viewform')


def updateData(request, id):
    pi = Student.objects.get(pk=id)
    form = forms.FormName(instance=pi)
    if request.method == "POST":
        pi = Student.objects.get(pk=id)
        form = forms.FormName(request.POST, instance=pi)
        if form.is_valid():
            form.save()
        else:
            pi = Student.objects.get(pk=id)
            form = forms.FormName(request.POST, instance=pi)
    return render(request, 'manualupload/updateform.html', {'id': id, 'form': form})
