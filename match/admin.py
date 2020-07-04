from django.contrib import admin
from .models import Judges, Player, Grades
# Register your models here.
admin.site.site_title = "农委会"
admin.site.site_header = "比赛投票系统"

admin.site.register(Judges)
admin.site.register(Player)
admin.site.register(Grades)