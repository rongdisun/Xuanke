from django.urls import path
from . import views

app_name = "manager"

urlpatterns = [
    path("teacher_add/", views.teacher_add, name="teacher_add"),
    path("teacher_list/", views.teacher_list, name="teacher_list"),
    path("student_add/", views.student_add, name="student_add"),
    path("student_list/", views.student_list, name="student_list"),
    path("user_del/", views.user_delete, name="user_del"),
    path("user_update/", views.user_update, name="user_update"),
    path("uploadAvatar", views.upload_avatar, name="avatar"),
    path("addUser", views.add_user, name="add_user"),
    path("verify_teacher_course", views.verify_teacher_course, name="verify_teacher_course"),
    path("verified_course", views.verified_course, name="verified_course"),
    path("verify_stu_select_course", views.verify_stu_select_course, name="verify_stu_select_course"),
    path("verified_stu_select_course", views.verified_stu_select_course, name="verified_stu_select_course"),
    path("user_detail/<str:userid>", views.user_detail, name="user_detail"),
]
