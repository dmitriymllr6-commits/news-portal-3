import json
import os
from datetime import date, datetime
from django.http import Http404
from .forms import NewsForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import News
from .forms import NewsForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden

DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    'data',
    'news.json'
)


def load_news():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f)

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_news(news_list):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(
            news_list,
            f,
            ensure_ascii=False,
            indent=2
        )




def home_view(request):

    news_list = News.objects.all().order_by('-date_created')

    return render(
        request,
        'home.html',
        {
            'news_list': news_list
        }
    )



def news_detail_view(request, news_id):

    news = get_object_or_404(News, id=news_id)

    return render(
        request,
        'news_detail.html',
        {'news': news}
    )


@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def profile_delete_view(request):

    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('home')

    return render(request, 'profile_delete.html')

@login_required
def add_news_view(request):

    if request.method == 'POST':

        form = NewsForm(request.POST)

        if form.is_valid():

            news = form.save(commit=False)

            news.author = request.user

            news.save()

            return redirect('success')

    else:
        form = NewsForm()

    return render(
        request,
        'add_news.html',
        {'form': form}
    )

def news_edit_view(request, news_id):

    news = get_object_or_404(News, id=news_id)

    if news.author != request.user:
        return HttpResponseForbidden("Нет доступа")

    if request.method == 'POST':

        form = NewsForm(request.POST, instance=news)

        if form.is_valid():
            form.save()
            return redirect('detail', news_id=news.id)

    else:
        form = NewsForm(instance=news)

    return render(request, 'news_form.html', {
        'form': form
    })

def news_delete_view(request, news_id):

    news = get_object_or_404(News, id=news_id)

    if news.author != request.user:
        return HttpResponseForbidden("Нет доступа")

    if request.method == 'POST':
        news.delete()
        return redirect('home')

    return render(request, 'news_confirm_delete.html', {
        'news': news
    })

def success_view(request):
    return render(request, 'success.html')

def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:

        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )