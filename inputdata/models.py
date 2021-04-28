from django.db import models

# Create your models here.

class Post(models.Model):
	namakk = models.CharField(max_length=100, default='')
	alamat = models.CharField(max_length=200, default='')
	jumlahart = models.IntegerField(default=0)
	nomorhp = models.CharField(max_length=15, default='')
	latitude = models.CharField(max_length=10, default='')
	longitude = models.CharField(max_length=10, default='')

	def __str__(self):
		return "{}".format(self.namakk)