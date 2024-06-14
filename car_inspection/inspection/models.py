from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Car(models.Model):
    make = models.CharField(max_length=100, verbose_name='Марка производителя')
    model = models.CharField(max_length=100, verbose_name='Модель')
    year = models.IntegerField(verbose_name='Год выпуска')
    vin = models.CharField(max_length=17, unique=True, verbose_name='ВИН-номер')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    mileage = models.IntegerField(verbose_name='Пробег')
    registration_number = models.CharField(max_length=20, unique=True, verbose_name='Регистрационный номер')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=timezone.now)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Inspection(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')
    date = models.DateField(verbose_name='Дата')
    passed = models.BooleanField(null=True, default='False', verbose_name='Завершено')
    inspector_comments = models.TextField(blank=True, null=True, verbose_name='Коментарии инспектора')
    inspector = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inspections', null=True, blank=True, verbose_name='Инспектор')

    def __str__(self):
        return f"Inspection for {self.car} on {self.date}"

class ServiceRecord(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')
    service_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Service for {self.car} on {self.service_date}"

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    date_published = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

class RegistrationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')
    request_date = models.DateField(verbose_name='Дата')
    approved = models.BooleanField(default=False, verbose_name='Одобрен')
    request_type = models.CharField(max_length=50, verbose_name='Тип заявки', choices=[('register', 'Зарегистрировать'), ('deregister', 'Снять с учета')])

    def __str__(self):
        return f"{self.get_request_type_display()} request for {self.car} by {self.user}"