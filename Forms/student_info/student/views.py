from django.shortcuts import render, redirect
from .forms import StudentForm, StudentMarksForm

def student_form_view(request):
    if request.method == 'POST':    
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_form')  # Redirect to avoid form resubmission
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_marks_form_view(request):
    if request.method == 'POST':
        form = StudentMarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_marks_form')  # Redirect to avoid form resubmission
    else:
        form = StudentMarksForm()
    return render(request, 'student_marks_form.html', {'form': form})
