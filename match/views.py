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


class ScoreView(generic.ListView):
    template_name = 'match/score.html'
    context_object_name = 'players'

    def get_queryset(self):
        return Player.objects.all()


class SortView(generic.ListView):
    template_name = 'match/sort.html'

    def get_queryset(self):
        return Grades.objects.all()


def login(request):
    """登录页面"""
    # if request.user and request.user.is_authenticated:
        # return HttpResponseRedirect('login')

    # return render(request, 'match/login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        logger.debug(f'--------------------------------------------------------------用户名{username}, {password}')
        return redirect('/')
    return render(request, 'match/login.html')


def logout(request):
    pass