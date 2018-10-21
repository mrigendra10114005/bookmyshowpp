from hashlib import md5
from django.db import models
from django.core.exceptions import ValidationError


class Audience(models.Model):
	""" IN THIS MODEL WE CONTAIN USERNAME,PASSWORD,EMAIL,MOB_NO"""
	# USERNAME='username'
	# PASSWORD='password'
	# NAME='name'
	# MOBILE='mobile_number'
	username=models.CharField(max_length=50,unique=True,null=False)
	password=models.CharField(max_length=50,null=False)
	name=models.CharField(max_length=50)
	# mobile_number=models.CharField(max_length=10)
	#created_at=models.DateTimeField(auto_new_add=True,editable=False)
	#updated_at=models.DateTimeField(auto_now=True)
	# class Meta:
		# db_table="User_detail"
		# abstract=False
		# unique_together=['username','name']
		# ordering=['name']

class Movie(models.Model):
	name=models.CharField(max_length=100,null=False)
	language=models.CharField(max_length=50,null=False)
	director=models.CharField(max_length=50,null=False)
	actor=models.CharField(max_length=50,null=False)
	duration=models.CharField(max_length=25,null=False)

	# class Meta:
	# 	abstract=False
	# 	ordering=['name']

class Theatre(models.Model):
	name=models.CharField(max_length=50,unique=True,null=False)
	city=models.CharField(max_length=50,null=False)
	no_screen=models.CharField(max_length=5,null=False)

	# class Meta:
	# 	abstract=False
	# 	ordering=['no_screen']

class Review(models.Model):
	movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
	review_type=models.CharField(max_length=100)
	discription=models.CharField(max_length=100)
class Screen(models.Model):
	movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
	theatre=models.ForeignKey(Theatre,on_delete=models.CASCADE)
	totalseat=models.CharField(max_length=5)
	showime=models.DateTimeField(max_length=10)

class Seatbooking(models.Model):
	audience=models.ForeignKey(Audience,on_delete=models.CASCADE)
	screen=models.ForeignKey(Screen,on_delete=models.CASCADE)
	price=models.CharField(max_length=10)
	seatnumber=models.CharField(max_length=5)

class Employee(models.Model):
	name=models.CharField(max_length=100)
	companyName=models.CharField(max_length=100)
	category=models.CharField(max_length=20)




