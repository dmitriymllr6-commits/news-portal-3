import json
import os

from datetime import date

from django.shortcuts import render, redirect
from django.http import Http404

from .forms import NewsForm


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

    news_list = load_news()

    news_list.sort(
        key=lambda x: x['date'],
        reverse=True
    )

    return render(
        request,
        'home.html',
        {
            'news_list': news_list,
            'today': str(date.today())
        }
    )


def news_detail_view(request, news_id):

    news_list = load_news()

    for news in news_list:
        if news['id'] == news_id:
            return render(
                request,
                'news_detail.html',
                {'news': news}
            )

    raise Http404("Новость не найдена")


def add_news_view(request):

    if request.method == 'POST':

        form = NewsForm(request.POST)

        if form.is_valid():

            news_list = load_news()

            new_id = max(
                (n['id'] for n in news_list),
                default=0
            ) + 1

            news = {
                'id': new_id,
                'title': form.cleaned_data['title'],
                'summary': form.cleaned_data['summary'],
                'content': form.cleaned_data['content'],
                'date': str(date.today())
            }

            news_list.append(news)

            save_news(news_list)

            return redirect('success')

    else:
        form = NewsForm()

    return render(
        request,
        'add_news.html',
        {'form': form}
    )


def success_view(request):
    return render(request, 'success.html')