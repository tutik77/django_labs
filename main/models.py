from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Lecture(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название лекции')
    description = models.TextField(verbose_name='Краткое описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'