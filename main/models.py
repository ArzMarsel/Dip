from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator
from django.db import models


class Dish(models.Model):
    Type_list = (
        ('soda', 'Напитки'),
        ('desert', 'Десерты'),
        ('first', 'Первое'),
        ('salat', 'Салаты'),
        ('sec', 'Второе'),
        ("fast", "Фаст-фуд"),
        ("alco", "Алкоголь"),
        ("tuck", "Закуски"),
    )
    name = models.CharField('Name', max_length=30)
    info = models.TextField('Information')
    price = models.FloatField('Price')
    quantity = models.IntegerField(verbose_name='Кол-во:', blank=True, null=True)
    kind = models.CharField(verbose_name='Type:', max_length=30, choices=Type_list)


class DishImage(models.Model):
    image = models.ImageField('Image:', upload_to='product_image/')
    dishes = models.ManyToManyField(Dish, verbose_name='Dishes:')


class Connect(models.Model):
    Choices_list = (
        ('done', 'Заказано'),
        ('none', 'Заказать'),
        ('delivering', 'Доставляеться'),
        ('cooking', 'Готовиться'),
        ('accepted', 'Принят')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(verbose_name='Кол-во:', blank=True, null=True)
    status = models.CharField(verbose_name='Status:', max_length=30, choices=Choices_list)

    def disconnect(self, user):
        if self.user == user:
            self.delete()


class Payment(models.Model):
    card_number = models.IntegerField(verbose_name='Card-number', max_length=16, validators=[MinLengthValidator(16), MaxLengthValidator(16)])
    cvc = models.IntegerField(verbose_name='CVC', max_length=3, validators=[MinLengthValidator(3), MaxLengthValidator(3)])
    date = models.DateField(verbose_name='Date', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    price = models.FloatField('Price', validators=[MinValueValidator(1)])