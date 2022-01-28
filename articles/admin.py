from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import ArtPage, Category, Tag, Article

class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

admin.site.register(ArtPage)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)