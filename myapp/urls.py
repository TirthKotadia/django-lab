from django.urls import path
from . import views


urlpatterns = [
    path(
        "students/",
        views.student_list,
        name="student_list"
    ),
    path(
        "students/<int:student_id>/",
        views.student_detail,
        name="student_detail"
    ),
]