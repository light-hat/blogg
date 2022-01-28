from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleView.as_view()),
    path('tags/', views.ArticleFilterView.as_view(), name="tags"),
    path('category/', views.CategoryView.as_view(), name="category"),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name="article_detail")
]