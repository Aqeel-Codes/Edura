from django.http import HttpResponse
from django.shortcuts import render , redirect, get_object_or_404
from .forms import StudentForm
from .models import Student

def home_page(request):
    return HttpResponse("<h1>Welcome to the Edura School Management System!</h1>")

def student_list(request):
    students = Student.objects.all()

    context = {
        'students': students,
    }
    return render(request, 'list.html', context)

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('school_management:student_list')  
    elif request.method == 'GET':
        form = StudentForm()

    context = {
        'form': form,
        'title': 'Add New Student',
    }
    return render(request, 'form.html', context)

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('school_management:student_list')  
    elif request.method == 'GET':
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'title': 'Update Student',
    }
    return render(request, 'form.html', context)

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('school_management:student_list')




