from django.db import models

# 评委
class Judges(models.Model):
    judge_name = models.CharField('评委姓名', max_length=20)
    judge_password = models.CharField('密码', max_length=30)

    class Meta:
        app_label = 'match'
        verbose_name = "评委"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.judge_name



# 选手
class Player(models.Model):
    player_name = models.CharField('选手姓名', max_length=20)

    class Meta:
        app_label = 'match'
        verbose_name = "选手"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.player_name

# 选手得分及场次
class Grades(models.Model):
    player_id = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    judge_id = models.ForeignKey(to=Judges, on_delete=models.CASCADE)
    score = models.FloatField('评委评分', default=0)
    rounds = models .IntegerField('场次')

    class Meta:
        app_label = 'match'
        verbose_name = "得分"
        verbose_name_plural = verbose_name
