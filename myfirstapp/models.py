from django.db import models

class ComputerModel(models.Model):
    class Meta:
        db_table = "computer"
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    RAM = models.IntegerField()
    CPU = models.IntegerField()
    monitor = models.IntegerField()