from django.shortcuts import get_object_or_404, redirect, render
from app.models import Student
# Create your views here.
def addStudent(request):
    student=request.POST['addStudent']
    Student.objects.create(student=student)
    return redirect('home')
def mark_as_paid(request,pk):
    student=get_object_or_404(Student,pk=pk)
    student.is_paid=True
    student.save()
    return redirect('home')
def mark_as_unpaid(request,pk):
    student=get_object_or_404(Student,pk=pk)
    student.is_paid=False
    student.save()
    return redirect('home')
def edit_student(request,pk):
    get_student=get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        new_student=request.POST['student']
        get_student.student=new_student
        get_student.save()
        return redirect('home')
    else:
        context={
            'get_student':get_student,
        }
        return render(request,'edit_student.html',context)
def delete_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    student.delete()
    return redirect('home')
