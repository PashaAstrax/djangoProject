from django.db import models
from django.core import validators as V

class CarModel(models.Model):
    class Meta:
        db_table = "cars"
        verbose_name = "cars"
        verbose_name_plural = "car"

    brand = models.CharField(max_length=20, validators=[V.MinLengthValidator(3), V.MaxLengthValidator(20)]) # unique=True, default="Honda", null=True, blank=True
    model = models.CharField(max_length=20)
    year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(2021)])

    def __str__(self):
        return self.brand