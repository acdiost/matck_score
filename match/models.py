from django.db import models

# 评委
class Judges(models.Model):
    judge_id = models.PositiveIntegerField(verbose_name="评委id", blank=False, null=False)
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
    player_id = models.PositiveIntegerField(verbose_name="选手id", blank=False, null=False)
    player_name = models.CharField('选手姓名', max_length=20)

    class Meta:
        app_label = 'match'
        verbose_name = "选手"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.player_name

# 选手得分及场次
class Grades(models.Model):
    player_name = models.CharField(verbose_name="选手姓名",  max_length=20, blank=False, null=False)
    judge_id = models.PositiveIntegerField(verbose_name="评委id", blank=False, null=False)
    score = models.FloatField('评委评分', default=0)
    # 0 未评分，1 已评分
    rated = models .PositiveIntegerField('是否评分', default=0)

    class Meta:
        app_label = 'match'
        verbose_name = "得分"
        verbose_name_plural = verbose_name
