from django.urls import path
from . import views

app_name = "teacher"

urlpatterns = [
    path("release_course/", views.release_course, name="release_course"),
    path("release_result/", views.release_result, name="release_result"),
    path("selected_stu/", views.selected_stu, name="selected_stu"),
]
