from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.

from .models import Student


def student_list(request):
    students = Student.objects.all()

    output = "<h1>Student List</h1>"

    for student in students:
        output += (
            f"<p>{student.name} - "
            f"Roll No: {student.roll_number} - "
            f"Age: {student.age}</p>"
        )

    return HttpResponse(output)


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    return HttpResponse(
        f"<h1>{student.name}</h1>"
        f"<p>Roll Number: {student.roll_number}</p>"
        f"<p>Age: {student.age}</p>"
    )