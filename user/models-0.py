from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.

class User(models.Model):
    userid = models.CharField(primary_key=True, max_length=20)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=10, default='student')
    c_time = models.DateTimeField(auto_now_add=True)
    avatar = models.CharField(max_length=255, default="/static/avatar/avatar.png")

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Course(models.Model):
    cid = models.CharField(primary_key=True, max_length=20)
    cname = models.CharField(max_length=20, unique=True)
    classroom = models.CharField(max_length=20)
    frequency = models.CharField(max_length=20)
    ctime = models.CharField(max_length=100)
    num = models.IntegerField(default=30)  # 开课人数
    status = models.IntegerField(default=0)  # 审核状态
    uid = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "课程"

    def __str__(self):
        return self.cname


class StuCourse(models.Model):

    cid = models.ForeignKey(Course, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)  # 默认是待审核状态，待管理员审核后改为1

    def __str__(self):
        if self.status == -1:
            return "未通过"
        elif self.status == 0:
            return "待审核"
        else:
            return "已通过"

