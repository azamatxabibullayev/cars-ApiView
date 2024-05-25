from django.db import models


# Create your models here.
class CategoryCars(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category_cars'

    def __str__(self):
        return self.name


class Cars(models.Model):
    category = models.ForeignKey(CategoryCars, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.FileField(upload_to='videos', blank=True, null=True)
    audio = models.FileField(upload_to='audio', blank=True, null=True)
    dock = models.FileField(upload_to='dock', blank=True, null=True)

    class Meta:
        db_table = 'cars'

    def __str__(self):
        return f'{self.category.name} | {self.name}'
