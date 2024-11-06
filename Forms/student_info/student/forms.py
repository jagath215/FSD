from django import forms
from .models import Student, StudentMarks

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'phone_number', 'hobbies']

class StudentMarksForm(forms.ModelForm):
    class Meta:
        model = StudentMarks
        fields = ['student', 'marks']
