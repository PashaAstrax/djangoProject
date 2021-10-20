from django.db import models
from django.core import validators as V

class PlaneModel(models.Model):
    class Meta:
        db_table = "planes"

        # verbose_name = "planes"
        # verbose_name_plural = "plane"

    brand = models.CharField(max_length=20, validators=[V.MinLengthValidator(2), V.MaxLengthValidator(20)]) # unique=True, default="Honda", null=True, blank=True
    model = models.CharField(max_length=20, validators=[V.MinLengthValidator(1), V.MaxLengthValidator(20)])
    year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(2021)])
    weight = models.FloatField(validators=[V.MinValueValidator(20000), V.MaxValueValidator(80000)])
    max_speed = models.FloatField(validators=[V.MinValueValidator(300), V.MaxValueValidator(1000)])
    seat_place = models.IntegerField(validators=[V.MinValueValidator(10), V.MaxValueValidator(300)])


    # def __str__(self):
    #     return self.brand