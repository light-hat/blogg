from django.shortcuts import render
from django.views.generic.base import View
from .models import Page

from articles.models import Category, Article

class HomePageView(View):
    def get(self, request):
        page = Page.objects.all()
        category = Category.objects.all()
        articles = Article.objects.all()[:3]
        return render(request, 'main/page.html', { 'page': page[0], 'category': category, 'arts': articles })