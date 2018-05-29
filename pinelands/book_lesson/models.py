from django.db import models
from django.contrib.auth.models import User
# Create your models here.


	
Gender_Options = (
	('MALE', 'Male'),
	('FEMALE', 'Female'),
	('OTHER', 'Other'),
)


class Student(models.Model):
	username = models.OneToOneField(User)
	email = models.CharField(max_length=128, unique=True)
	FirstName = models.CharField(max_length=128)
	LastName = models.CharField(max_length=128)
	DOB = models.DateField()
	Gender = models.CharField(max_length=128, choices = Gender_Options)
	phonenumber = models.CharField(max_length=128)
	facebookID = models.URLField()
	
	def __str__(self):
		return self.email
		


class Parent(models.Model):
	username = models.OneToOneField(User)
	email = models.CharField(max_length=128, unique=True)
	FirstName = models.CharField(max_length=128)
	LastName = models.CharField(max_length=128)
	DOB = models.DateField()
	Gender = models.CharField(max_length=128, choices = Gender_Options)
	phonenumber = models.CharField(max_length=128)
	parentof = models.CharField(max_length=128)
	
	def __str__(self):
		return self.email

class Teacher(models.Model):
	username = models.OneToOneField(User)
	email = models.CharField(max_length=128, unique=True)
	FirstName = models.CharField(max_length=128)
	LastName = models.CharField(max_length=128)
	DOB = models.DateField()
	Gender = models.CharField(max_length=128, choices = Gender_Options)
	phonenumber = models.CharField(max_length=128)
	LanguagesKnown = models.CharField(max_length=128)
	qualifications = models.TextField()
	
	def __str__(self):
		return self.email

class Lesson(models.Model):
	Teacher = models.ForeignKey(Teacher)
	Student = models.ForeignKey(Student)
	Date = models.DateField()
	Instrument = models.CharField(max_length=128)
	Language = models.CharField(max_length=128)
	def __str__(self):
		return self.email
		
		
