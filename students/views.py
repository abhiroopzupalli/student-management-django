from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Student
from .forms import StudentForm


def student_list(request):
    """List all students, with simple search by name / roll no / department."""
    query = request.GET.get('q', '').strip()
    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(name__icontains=query)
            | Q(roll_no__icontains=query)
            | Q(department__icontains=query)
        )

    context = {
        'students': students,
        'query': query,
        'total': students.count(),
    }
    return render(request, 'students/student_list.html', context)


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form, 'title': 'Add Student'})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {'form': form, 'title': 'Edit Student'})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully.')
        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {'student': student})
