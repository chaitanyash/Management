from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

#Parent Model
class Parent(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	contact = models.BigIntegerField(max_length=10)
	address = models.CharField(max_length=500)

	def __str__(self):
		return self.user.first_name+' '+self.user.last_name

class Student(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=500)
	contact = models.BigIntegerField(max_length=10)
	parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.first_name+' '+self.user.last_name +' Son of '+self.parent.user.first_name+' '+self.parent.user.last_name

#Student

#Department Modal
class Department(models.Model):
	name = models.CharField(max_length=80, unique=True)

	def __str__(self):
		return self.name;

class Course(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    department = models.ForeignKey(Department ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.department.name
