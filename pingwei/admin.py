from django.contrib import admin

# Register your models here.
from pingwei.models import Judges

admin.site.site_title = "农委会"
admin.site.site_header = "比赛投票系统"

admin.site.register(Judges)
