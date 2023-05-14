from django import forms
from .models import User, Course, StuCourse


class LoginModelForm(forms.Form):
    userid = forms.CharField(required=True)
    password = forms.CharField(required=True)


class UserModelForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = ["c_time", "last_login"]


class CourseModelForm(forms.ModelForm):

    class Meta:
        model = Course
        exclude = ["status"]
