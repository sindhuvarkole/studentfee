from django.urls import path
from . import views

urlpatterns = [
    path('addStudent/',views.addStudent,name='addStudent'),
    path('mark_as_paid/<int:pk>/',views.mark_as_paid,name='mark_as_paid'),
    path('mark_as_unpaid/<int:pk>/',views.mark_as_unpaid,name='mark_as_unpaid'),
    path('delete_student/<int:pk>/',views.delete_student,name='delete_student'),
    path('edit_student/<int:pk>/',views.edit_student,name='edit_student'),
]