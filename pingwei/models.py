from django.db import models


# Create your models here.
class Judges(models.Model):
    judge_name = models.CharField('评委姓名', max_length=20)
    judge_password = models.CharField('密码', max_length=30)
