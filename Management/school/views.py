from django.shortcuts import render
from django.conf.urls import url,include
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser,FormParser
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


#DepartmentApi()
@csrf_exempt
def departmentApi(request):
	if request.method == 'GET':
		department = Department.objects.all()
		serializer = DepartmentSerializer(department, many=True)
		return JsonResponse(serializer.data,safe=False)
	elif request.method == 'POST':
		#Declaring data which will be useful to store a dictionary

		data=''
		if 'name' in request.POST:
			data = {'name':request.POST['name']}
		else:
			return JsonResponse({'error': 'Please pass department name'},
            status=status.HTTP_400_BAD_REQUEST)	

		serializer = DepartmentSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)
#End departmentApi

#courseApi()
@csrf_exempt
def courseApi(request):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated,)
	if request.method == 'GET':
		if request.GET.get('name'):
			print(request.GET0.get('name'))
			course = Course.objects.filter(name=request.GET.get('name'))
		elif request.GET.get('duration'):
			print(request.GET.get('duration'))
			course = Course.objects.filter(duration__gte=request.GET.get('duration'))
		else:	
			course = Course.objects.all()
		serializer = CourseSerializer(course, many=True)
		return JsonResponse(serializer.data,safe=False)
	elif request.method == 'POST':
		#Declaring data which will be useful to store a dictionary
		data=''
		if ('name' in request.POST and 'duration' in request.POST and 'department_id' in request.POST) :
			data = {'name':request.POST['name'],
					'duration':request.POST['duration'],
					'department_id':request.POST['department_id']}
		else:
			return JsonResponse(
            {'error': 'Please pass name, duration, department_id'},
            status=status.HTTP_400_BAD_REQUEST)		
		serializer = CourseSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)
#End courseApi


#Parent API only GET for now
@csrf_exempt
def parentApi(request):
	#Checking if data is coming from GET method
	if request.method == 'GET':
		if 'username' in request.GET:
			try: #to handle exception
				parents = Parent.objects.get(user = User.objects.get(username = request.GET['username']))
				serializer = ParentSerializer(parents)
				print(parents)
			except ObjectDoesNotExist:
				return JsonResponse(
            {'error': 'No data found for user '+request.GET['username']},
            status=status.HTTP_200_OK)
		else:	
			parents = Parent.objects.all()
			serializer = ParentSerializer(parents, many=True)
		return JsonResponse(serializer.data,safe=False)
	elif request.method == 'POST': #Checking if Data is coming from POST
		if request.user.is_staff or request.user.is_superuser:
			data=''
			if ('username' in request.POST and 'password' in request.POST and 'email' in request.POST and 'first_name' in request.POST and
				 'last_name' in request.POST and 'contact' in request.POST and 'address' in request.POST):
				user = User.objects.create_user(username = request.POST['username'],
					password = request.POST['password'],email = request.POST['email'],first_name = request.POST['first_name'],
					last_name = request.POST['last_name'])
				data = {'user':user.id,'contact':request.POST['contact'],'address':request.POST['address']}
			else:
				return JsonResponse(
	            {'error': 'Please pass name, duration, department_id'},
	            status=status.HTTP_400_BAD_REQUEST)		
			serializer = ParentSerializer(data=data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse(serializer.data, status=201)
			return JsonResponse(serializer.errors, status=400)
		else:
			return JsonResponse(
	            {'error': 'You are not authorized to do this Operation'},
	            status=status.HTTP_400_BAD_REQUEST)	            
#End Parent API

#login Api
@csrf_exempt
def loginApi(request):
	#Checking if data is coming from POST method
	if request.method.POST:
		if ('username' in request.POST and 'password' in request.POST):
			#You have username and password in POST
			user = authenticate(username=username, password=password)
			# import pdb; pdb.set_trace()
			#Cheking if we got any user or not
			if user is not None:
				login(request, user)
				return Response({'message':'success'}, status=status.HTTP_200_OK)

			return Response({'message': 'login failed'}, status=status.HTTP_400_BAD_REQUEST)
		else:
			#username and Password not provided, returning error
			return JsonResponse({'error':'Please provide username and Password '},status=STATUS_400_BAD_REQUEST)	
#End login Api