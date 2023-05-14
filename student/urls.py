from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path("course_list/", views.course_list, name="course_list"),
    path("selected_course/", views.selected_course, name="selected_course"),
    path("select_course/", views.select_course, name="select_course"),
    path("selected_notice/", views.selected_notice, name="selected_notice"),
    path("course_detail/<str:c_id>", views.course_detail, name="course_detail"),


]
