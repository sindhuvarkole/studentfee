from django.shortcuts import render
from app.models import Student

def home(request):
    students=Student.objects.filter(is_paid=False).order_by('-updated_at')
    paid_students=Student.objects.filter(is_paid=True)
    context={
        'students':students,
        'paid_students':paid_students
    }
    return render(request,'home.html',context)