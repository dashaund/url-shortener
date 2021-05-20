from django.db import models

# Create your models here.


class Customer(models.Model):
	url = models.CharField(max_length=255)
	return url
