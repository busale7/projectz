from django.db import models
#nested tuple
platform_choices =(
		("PC","PC"),
		("playstation","playstation"),
		("xbox","xbox"),
	)
# Create your models here.
class Captain(models.Model):
	name = models.CharField(max_length=125)
	release_date= models.DateField()
	platforms =models.CharField(max_length=100 ,choices=platform_choices)
	multiplayer = models.BooleanField(default=False)
	image = models.ImageField(null=True)

	def __str__(self):
		return self.name
		
