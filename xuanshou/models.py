from django.db import models


# Create your models here.
class Player(models.Model):
    username = models.CharField('选手姓名', max_length=20)
    score = models.FloatField('选手得分')

    def __str__(self):
        return self.username, self.score
