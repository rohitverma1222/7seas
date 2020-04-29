from django.db import models

# Create your models here.
class des(models.Model):
	name=models.CharField(max_length=30,null=True,)
	img1=models.ImageField(upload_to='pics',null=True)
	img2=models.ImageField(upload_to='pics',null=True)
	img3=models.ImageField(upload_to='pics',null=True)
	img4=models.ImageField(upload_to='pics',null=True)
	category=models.CharField(max_length=20,null=True)

	descrip=models.CharField(max_length=200,null=True)
	big_descrip=models.CharField(max_length=900,null=True)
	place_under=models.CharField(max_length=30,null=True)
	total_day=models.IntegerField(null=True)
	total_night=models.IntegerField(null=True)
	price=models.IntegerField()


def __str__(self):
	return self.name

class com(models.Model):
	name=models.CharField(max_length=30,null=True)
	comments=models.CharField(max_length=100,null=True)

def __str__(self):
	return self.name

class coments(models.Model):
	name=models.CharField(max_length=30,null=True)
	comments=models.CharField(max_length=100,null=True)

def __str__(self):
	return self.name