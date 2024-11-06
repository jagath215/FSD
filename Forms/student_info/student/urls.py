from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_form_view, name='student_form'),
    path('marks/', views.student_marks_form_view, name='student_marks_form'),
]
