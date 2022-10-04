from django.db import models

class Category(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    # def __str__(self):
    #     return "Вася Пупкин"


class Service(models.Model):
    title = models.CharField(max_length=150,verbose_name='Название услуги')
    price = models.IntegerField()
    category = models.ForeignKey("Category",on_delete=models.CASCADE,related_name="services")

    # def __str__(self):
    #     return self.title

