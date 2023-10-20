from django.db import models

# Create your models here.

class Professia (models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    def __str__(self):
        return self.title

    def get_field(self):
        return [(field.name, field.value_to_string(self)) for field in Professia._meta.fields]



class Skill (models.Model):
    name = models.TextField(max_length=50, verbose_name="Название")

    class Meta:
        ordering = ["-name"]
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name

    def get_field(self):
        return [(field.name, field.value_to_string(self)) for field in Skill._meta.fields]


class Questions (models.Model):
    text_question = models.TextField(max_length=50, verbose_name="Название")
    point = models.IntegerField(verbose_name="Очки")
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, verbose_name="Навык")

    class Meta:
        ordering = ["-text_question"]
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text_question

    def get_field(self):
        return [(field.name, field.value_to_string(self)) for field in Questions._meta.fields]


class Model_profession (models.Model):
    professia = models.ForeignKey(Professia, on_delete=models.PROTECT, verbose_name="Профессия")
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, verbose_name="Навык")
    number_of_points = models.IntegerField(verbose_name="Количество очков")

    class Meta:
        ordering = ["-professia"]
        verbose_name = "Модель профессии"
        verbose_name_plural = "Модели профессий"

    def __str__(self):
        return self.professia

    def get_field(self):
        return [(field.name, field.value_to_string(self)) for field in Model_profession._meta.fields]


class Answers (models.Model):
    professia = models.ForeignKey(Professia, on_delete=models.PROTECT, verbose_name="Профессия")
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, verbose_name="Навык")
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


class Empty_certificate (models.Model):
    certificate = models.TextField(max_length= 200, verbose_name= "Сертификат")
    full_file = models.FileField (verbose_name="Все файлы")
    one_file = models.FileField(verbose_name="Один файл")

    class Meta:
        ordering = ["-certificate"]
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

    def __str__(self):
        return self.certificate

    def get_field(self):
        return [(field.name, field.value_to_string(self)) for field in Empty_certificate._meta.fields]