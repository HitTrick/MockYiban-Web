from django.db import models

# Create your models here.


class StudentRecord(models.Model):
    in_out = models.CharField(max_length=10, verbose_name="进/出", default="出")
    name = models.CharField(max_length=20, verbose_name="学生名字", default="未命名")
    stu_id = models.CharField(max_length=40, verbose_name="学号", default="200000000")
    gate = models.CharField(max_length=20, verbose_name="校门", default="南门")