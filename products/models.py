from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=255)


class Offer(models.Model):
    code=models.CharField(max_length=10)
    desccription=models.CharField(max_length=255)
    discount=models.FloatField()