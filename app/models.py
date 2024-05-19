from django.db import models

# Create your models here.
class Student(models.Model):
    student=models.CharField(max_length=250)
    is_paid=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student