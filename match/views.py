from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Judges, Player, Grades
import logging

logger = logging.getLogger('default')

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'match/index.html'
    context_object_name = 'judges'

    def get_queryset(self):
        return Judges.objects.all()


class JudgeView(generic.ListView):
    template_name = 'match/judge_list.html'
    context_object_name = 'judges'

    def get_queryset(self):
        return Judges.objects.all()


class PlayerView(generic.ListView):
    template_name = 'match/player_list.html'
    context_object_name = 'players'

    def get_queryset(self):
        return Player.objects.all()


class SortView(generic.ListView):
    template_name = 'match/sort.html'

    def get_queryset(self):
        return Grades.objects.all()


def score(request):
    """打分页面"""
    if request.method == "POST":
        fengcai = request.POST.get('fengcai', None)
        kuaikou = request.POST.get('kuaikou', None)
        daihuo = request.POST.get('daihuo', None)
        judge_id = request.POST.get('judge_id', None)
        player_id = request.POST.get('player_id', None)
        logger.error(f'------------------------分数1：{fengcai}, 评委id：{judge_id}, 选手id：{player_id}')
        # TODO 选手得分计算及逻辑整理
    players = Player.objects.all()
    return render(request, 'match/score.html', {"players": players})


def login(request):
    """登录页面"""
    if request.session.get('is_login',None):
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        # 用户名和密码都不为空
        if username and password:
            logger.error(f'------------------------用户名：{username}, 密码：{password}')
            username = username.strip()
            try:
                user = Judges.objects.get(judge_name=username)
                if user.judge_password == password:
                    request.session['is_login'] = True
                    request.session['judge_id'] = user.id
                    request.session['judge_name'] = user.judge_name
                    return redirect('/score')
                else:
                    message = "密码不正确！"
            except Exception as e:
                message = "用户名不存在！"
                logger.error(f'登录异常：{e}')
        return render(request, 'match/login.html', {"message": message})
    return render(request, 'match/login.html')


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/")
    request.session.flush()
    return redirect("/")
