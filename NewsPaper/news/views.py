# render был импортирован по умолчанию, я не стала его удалять
from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-time_created'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # пусть это пока побудет здесь, вдруг пригодится
        # context['next_news'] = "Тут что-то должно быть написано. Зачем оно? Пусть будет!"
        context['news_number'] = Post.objects.all()
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'news_item.html'
    context_object_name = 'news_item'

