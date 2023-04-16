from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Vehicle(models.Model):
    CAPACITY_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    ]

    name = models.CharField(max_length=128, verbose_name='Название')
    photo = models.ImageField(verbose_name='Изображение')
    color = models.ForeignKey('Color', verbose_name='Цвет', null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Producer', verbose_name='Производитель', null=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField('Category', verbose_name='Категории', blank=True)
    price = models.IntegerField(verbose_name='Цена (рубли)')
    description = models.CharField(max_length=512, verbose_name='Описание')
    number = models.CharField(max_length=6, verbose_name='Номер')
    mileage = models.IntegerField(verbose_name='Пробег')
    capacity = models.IntegerField(choices=CAPACITY_CHOICES, verbose_name='Вместимость (человек)', default=4)

    def __str__(self):
        return f'{self.name}, {self.brand.name} ({self.color.name}, #{self.number})'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Bike(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    photo = models.ImageField(verbose_name='Изображение')
    color = models.ForeignKey('Color', verbose_name='Цвет', null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Producer', verbose_name='Производитель', null=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField('Category', verbose_name='Категории')
    price = models.IntegerField(verbose_name='Цена (рубли)')
    description = models.CharField(max_length=512, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}, {self.brand.name} ({self.color.name})'

    class Meta:
        verbose_name = 'Велосипед'
        verbose_name_plural = 'Велосипеды'


class Producer(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Color(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Drive(models.Model):
    class Tariff(models.IntegerChoices):
        MINUTES = 1
        HOURS = 2
        DAYS = 3
        SPECIAL = 4

    ACTIVE = 'active'
    FINISHED = 'finished'

    STATUS_CHOICES = [
        (ACTIVE, "Активный"),
        (FINISHED, "Завершенный")
    ]

    total = models.IntegerField(verbose_name='Сумма')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    tariff = models.IntegerField(choices=Tariff.choices, verbose_name='Тариф')
    driver = models.ForeignKey(User, verbose_name='Арендатор', null=True, on_delete=models.SET_NULL)
    vehicle = models.ForeignKey(Vehicle, verbose_name='Автомобиль', blank=True, null=True, on_delete=models.SET_NULL)
    bike = models.ForeignKey(Bike, verbose_name='Велосипед', blank=True, null=True, on_delete=models.SET_NULL)
    duration = models.TimeField(verbose_name='Длительность', null=True, blank=True)
    status = models.CharField(max_length=10, verbose_name='Статус', choices=STATUS_CHOICES)
    rating = models.IntegerField(verbose_name='Оценка', null=True, blank=True)

    def __str__(self):
        return f'Поездка #{self.pk}, {self.date.day}.{self.date.month}.{self.date.year}, {self.driver.first_name} '

    class Meta:
        verbose_name = 'Поездка'
        verbose_name_plural = 'Поездки'


class Feedback(models.Model):
    email = models.EmailField(verbose_name='Email')
    subject = models.TextField(verbose_name='Вопрос или проблема')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата обращения')
    user = models.ForeignKey(User, verbose_name='Пользователь', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Обращение #{self.pk} от {self.date}, {self.email}'

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'


class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    excerpt = models.CharField(max_length=128, verbose_name='Краткое описание')
    preview = models.ImageField(verbose_name='Изображение', null=True, blank=True)
    content = models.TextField(verbose_name='Содержание статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, verbose_name='Автор', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'