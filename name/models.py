from django.db import models

# Create your models here.
class name(models.Model):
	name = models.CharField(max_length=32)
	mail = models.TextField()
	def __str__(self):
		return self.name
