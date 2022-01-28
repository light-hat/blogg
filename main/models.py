from django.db import models

class PersonalData(models.Model):
    '''Эта модель описывает одну строчку из краткого резюме'''
    title = models.CharField("Заголовок", max_length=50, default="")
    icon = models.CharField("Имя иконки в фреймворке", max_length=40, default="")
    text = models.CharField("Текст", max_length=100, default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Строчка"
        verbose_name_plural = "Личные данные"

class MenuIcon(models.Model):
    '''Модель, описывающая иконки, которые отображаются в меню'''
    title = models.CharField("Заголовок", max_length=50, default="")
    icon = models.CharField("Имя иконки в фреймворке", max_length=40, default="")
    tooltip = models.CharField("Всплывающая подсказка", max_length=50, default="")
    link = models.CharField("Ссылка", max_length=50, default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Иконка меню"
        verbose_name_plural = "Иконки меню"

class Page(models.Model):
    '''Эта модель описывает главную страницу'''
    title = models.CharField("Заголовок", max_length=50, default="")
    subtitle = models.CharField("Подзаголовок", max_length=100, default="")

    icons = models.ManyToManyField(MenuIcon, verbose_name="Иконки меню")

    quote = models.TextField("Цитата", default="")
    author = models.CharField("Автор цитаты", max_length=70, default="")

    avatar = models.ImageField("Аватар", upload_to="main_page/")
    about = models.ManyToManyField(PersonalData, verbose_name="Личные данные")

    footer = models.TextField("Футер", default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройки главной страницы"
        verbose_name_plural = "Настройки главной страницы"