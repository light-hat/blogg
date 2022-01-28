from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Article, Category, ArtPage
from main.models import Page
from bs4 import BeautifulSoup

class ArticleView(ListView):
    '''Отображаем список статей'''
    model = Article
    queryset = Article.objects.all().order_by("-id")

    paginate_by = 8
    template_name = "articles/article_list.html"

    def get_context_data(self, **kwargs):
        context = super(__class__, self).get_context_data(**kwargs)
        context['core'] = Page.objects.all()[0]
        context['page'] = ArtPage.objects.all()[0]
        context['category'] = Category.objects.all()
        
        return context

class ArticleFilterView(ArticleView, ListView):
    '''Фильтр статей'''
    def get_queryset(self):
        queryset = Article.objects.filter(
                tags__in=self.request.GET.getlist("id")
            ).distinct()

        return queryset

class CategoryView(ArticleView, ListView):
    '''Фильтр категорий'''

    def get_queryset(self):
        queryset = Article.objects.filter(
                category__in=self.request.GET.getlist("id")
            ).distinct()

        return queryset

class ArticleDetailView(DetailView):
    '''Отображаем полную статью'''
    model = Article
    slug_field = "id"
    
    def get_context_data(self, **kwargs):
        context = super(__class__, self).get_context_data(**kwargs)
        context['core'] = Page.objects.all()[0]
        context['category'] = Category.objects.all()

        return context