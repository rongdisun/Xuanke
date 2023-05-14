from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("index/", views.index_page, name="index"),
    path("user_logout/", views.user_logout, name="user_logout"),

]
