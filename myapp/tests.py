from django.test import TestCase
from django.urls import reverse

# Create your tests here.

from .models import Student 

class StudentModelTest(TestCase):

    def test_student_creation(self):
        student = Student.objects.create(
            name="Rahul",
            roll_number=101,
            age=20
        )

        self.assertEqual(student.name, "Rahul")
        self.assertEqual(student.roll_number, 101)
        self.assertEqual(student.age, 20)

    def test_student_string(self):
        student = Student.objects.create(
            name="Rahul",
            roll_number=101,
            age=20
        )

        self.assertEqual(str(student), "Rahul")

    def test_student_count(self):
        Student.objects.create(
            name="Rahul",
            roll_number=101,
            age=20
        )

        self.assertEqual(Student.objects.count(), 1)


class StudentViewTest(TestCase):

    def setUp(self):
        self.student = Student.objects.create(
            name="Rahul",
            roll_number=101,
            age=20
        )

    def test_student_list_view(self):
        response = self.client.get(
            reverse("student_list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rahul")

    def test_student_detail_view(self):
        response = self.client.get(
            reverse(
                "student_detail",
                args=[self.student.id]
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rahul")
        self.assertContains(response, "101")
        self.assertContains(response, "20")