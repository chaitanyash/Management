from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

#Department Serializer
class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = '__all__'

#Course Serializer
class CourseSerializer(serializers.ModelSerializer):

	department = DepartmentSerializer(read_only=True)
	department_id = serializers.IntegerField(write_only=True)

	class Meta:
		many=True
		model = Course
		fields = ('id','name','duration','department','department_id')
		# depth = 1
	# department_name = DepartmentSerializer()

#Parent Srializer
class ParentSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source='user.username',read_only=True)
	email = serializers.CharField(source='user.email',read_only=True)
	password = serializers.CharField(source='user.password',read_only=True)
	first_name = serializers.CharField(source='user.first_name',read_only=True)
	last_name = serializers.CharField(source='user.last_name',read_only=True)

	class Meta:
		many = True
		model = Parent
		fields = '__all__'

