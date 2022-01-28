from django.db import models
from datetime import date

from django.urls import reverse

class Category(models.Model):
    '''Категория статей'''
    title = models.CharField("Название категории", max_length=100, default="")
    description = models.TextField("Краткое описание", default="")
    icon = models.ImageField("Иконка 48x48", upload_to="category_icons")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Tag(models.Model):
    '''Теги, что-то вроде подкатегорий'''
    title = models.TextField("Тег", default="")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Article(models.Model):
    '''Данная модель описывает публикацию на сайте'''
    title = models.CharField("Заголовок публикации", max_length=120, default="")
    subtitle = models.TextField("Подзаголовок", default="")

    category = models.ManyToManyField(Category, verbose_name="Категория")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")

    published = models.DateField(verbose_name="Дата публикации", default=date.today())

    text = models.TextField("Основная статья")
    contents = models.TextField("Оглавление", default="<li><a href=\"#content\">Ссылка на главный заголовок</a><ul><li><a href=\"#link\">Заголовок в статье</a></li><ul><li><a href=\"#link\">Подзаголовок</a></li></ul></ul></li>")

    meta_keywords = models.TextField(verbose_name="Ключевые слова (метаданные)", default="")
    meta_description = models.TextField(verbose_name="Описание (метаданные)")

    meta_author = models.TextField(verbose_name="Автор (метаданные)", default="l1ghth4t")
    meta_copyright = models.TextField(verbose_name="Авторские права (метаданные)", default="Alexey Pirogov")

    disclaimer = models.TextField(verbose_name="disclaimer", default="none")

    background_image = models.ImageField(verbose_name="Фоновое изображение", upload_to="article_bgs/", default="")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.id})

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"

class ArtPage(models.Model):
    '''Данная модель описывает данные в каталоге статей'''
    title = models.CharField("Заголовок страницы", max_length=50, default="")
    subtitle = models.CharField("Подзаголовок", max_length=100, default="")
    disclaimer = models.TextField("Дисклеймер", default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройки новостной страницы"
        verbose_name_plural = "Настройки новостной страницы"