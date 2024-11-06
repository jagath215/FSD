from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    hobbies = models.TextField()

    def __str__(self):
        return self.name
    
class StudentMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.marks}"
