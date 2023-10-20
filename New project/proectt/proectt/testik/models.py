from django.contrib.auth.models import User
from django.db import models

from anketa.models import Professia, Skill


# Create your models here.

class Answers (models.Model):
    professia = models.ForeignKey(Professia, on_delete=models.PROTECT, verbose_name="Профессия", related_name ="professiaanswers")
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, verbose_name="Навык", related_name ="skillanswers")
    number_of_points = models.IntegerField (verbose_name="Количество очков")
    date = models.DateField (verbose_name="Дата прохождения")

    class Meta:
        ordering = ["-professia"]
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return self.professia

    def get_field(self):
        return [(field.name, field.value_to_string(self)) for field in Answers._meta.fields]


class Grajdanin(User):
    avatar = models.FileField(verbose_name="Аватар")
    number = models.TextField(verbose_name="Номер телефона")
    birthday = models.DateField(verbose_name="Дата рождения")

    class Meta:
        ordering = ["-username"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

    def get_field(self):
        return [(field.name, field.value_to_string(self)) for field in Grajdanin._meta.fields]


class Users_certificate (models.Model):
    certificate = models.IntegerField(verbose_name="Сертификат")
    grajdanin = models.ForeignKey(Grajdanin, on_delete=models.PROTECT, verbose_name="Пользователь")
    main_skill = models.TextField (verbose_name="Основной навык")
    all_skills = models.TextField (verbose_name="Все навыки")
    date_of_text = models.DateField (verbose_name="Дата")
    my_full_certificate = models.FileField(verbose_name="Мой полный сертификат")
    my_one_certificate = models.FileField(verbose_name="Мой одиночный сертификат")

    class Meta:
        ordering = ["-grajdanin"]
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

    def __str__(self):
        return self.grajdanin

    def get_field(self):
        return [(field.name, field.value_to_string(self)) for field in Users_certificate._meta.fields]