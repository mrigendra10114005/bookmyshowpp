import json
from django.http import JsonResponse
from django.views.decorators.http import *
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import Movie,Audience,Theatre,Review,Screen,Seatbooking,Employee

def index(request):
	"""
		this is for index
	"""
	return HttpResponse("Hello, world. You're at the bookmyshow index.")


def movieView(request):
	"""
		this method  is used to show data of movie table
	"""

	response_data = []
	movie_Set = Movie.objects.all()
	for movie in movie_Set:
		movie_list= {"movie_name": movie.name,"movie_language":movie.language,"movie_diector":movie.director,"movie_actor":movie.actor} 
		response_data.append(movie_list)
	data = json.dumps(response_data)
	return HttpResponse(data, content_type="application/json")



def audienceView(request):
	"""
		This method is used to show data of Audience table
	"""
	response_data = []
	audience_Set = Audience.objects.all()
	for people in audience_Set:
		people_list= {"audience": people.name,"screen":people.username,"seatnumber":people.password} 
		response_data.append(people_list)
	data = json.dumps(response_data)
	return HttpResponse(data, content_type="application/json")


def theatreView(request):
	"""
		This method is used to show  data of Theatre table 
	"""

	response_data = []
	theatre_Set = Theatre.objects.all()
	for theatre in theatre_Set:
		theatre_list= {"name": theatre.name,"city":theatre.city,"no_screen":theatre.no_screen} 
		response_data.append(theatre_list)
	data = json.dumps(response_data)
	return HttpResponse(data, content_type="application/json")


def reviewView(request):
	"""
		This method is used to show data of review table
	"""

	response_data = []
	review_Set = Review.objects.all()
	for review in review_Set:
		review_list = {"name": review.movie.name,"review_type":review.review_type,"discription":review.discription} 
		response_data.append(review_list)
	data = json.dumps(response_data)
	return HttpResponse(data, content_type="application/json")


def screenView(request):
	"""
		This method is used to show data of screen table
	"""

	response_data = []
	screen_Set = Screen.objects.all()
	for screen in screen_Set:
		screen_list = {" movie_name": screen.movie.name,"threatre_name":screen.theatre.name,"total_seat":screen.totalseat} 
		response_data.append(screen_list)
	data = json.dumps(response_data)
	return HttpResponse(data, content_type="application/json")


def seatbookingView(request):
	"""
		This method is used to show data of seatbooking
	"""
	response_data = []
	seatbooking_Set = Seatbooking.objects.all()
	for Seatbook in seatbooking_Set:
		r= {"audience": Seatbook.audience.name,"screen":Seatbook.screen.name,"totalseat":Seatbook.totalseat} 
		response_data.append(r)
	data = json.dumps(response_data)
	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def employeeview(request):
	"""
		this fuction create the data if none of data is missing or if all the data matchin with any other rowof table this this function will give tha data is already preaent
	"""
	if request.POST:
		Name = request.POST.get('name','not_present')
		company = request.POST.get('companyName','not_present')
		category = request.POST.get('category','not_present')
		if Name == 'not_present' or company == 'not_present' or category == 'not_present':
			data = [{"Exception":"One of  the data is missing"}]
		elif Employee.objects.get(name = Name) and Employee.objects.get(companyName = company) and Employee.objects.get(category = category) :
			data = [{"Expection": "Data is already present"}]
		else:
			empl_data = Employee.objects.create(name = Name,companyName = company,category = category)
			data = serializers.serialize('json',empl_data)
	else:
		all_emp = Employee.objects.all()
		data = serializers.serialize('json',all_emp)
	return HttpResponse(data,content_type = "application/json")
		

@csrf_exempt
def employeedelete(request,question_id):
	"""
		this function will delete the data from database if present present in database
	"""
	if request.method == 'DELETE':
		try:
			Employee.objects.get(id=question_id).delete()
			data = [{"Exception":"Employee is deleted"}]
		except:
			data = [{"Exception":"This Employee is Not prsent"}]
	else:
		data = [{"Exception":"Pls call delete Method"}]

	return HttpResponse(data,content_type="application/json")

@csrf_exempt
def employeeupdate(request,question_id):
	
	if request.method=='POST':
		try:
			t = Employee.objects.get(id=question_id)
			Name = request.POST.get('name','')
			Company = request.POST.get('company','')
			Category = request.POST.get('category','')
			t = Employee.objects.get(id=question_id)
			t.name = Name
			t.companyName = Company
			t.category = Category
			t.save()
			updated_emp = Employee.objects.get(id=question_id)
			data = serializers.serialize('json',[updated_emp])
		except:
			data=[{"Exception":"Person of this id is not prsent"}]
	else:
		data=[{"Exception":"Pls request  by post method"}]
	return HttpResponse(data,content_type="application/json")


@method_decorator(csrf_exempt, name='dispatch')
class employeeUpdateViews(TemplateView):

	"""This for fetching data and adding the data to the database"""

	def get(self, request):

		emp_obj = Employee.objects.all()
		data = serializers.serialize('json',[emp_obj])
		return HttpResponse(data,content_type="application/json")

	def post(self, request):
		
		if request.POST:
			Name=request.POST.get('name','')
			data=[{"Exception":"Employee already present"}]
			try:
				emp_obj=Employee.objects.get(name=Name)
			except:
				Company=request.POST.get('company','')
				Category=request.POST.get('category','')
				empl_data=Employee.objects.create(name=Name,companyName=Company,category=Category)
				data=serializers.serialize('json',[empl_data])
		else:
			all_emp=Employee.objects.all()
			data=serializers.serialize('json',[all_emp])
		return HttpResponse(data,content_type="application/json")


@method_decorator(csrf_exempt, name='dispatch')
class employeeUpdateView(TemplateView):

	"""this for update the table and delete the table """

	def delete(self,request,question_id):
		try:
			Employee.objects.get(id=question_id).delete()
			data =[{"Exception":"Employee is deleted"}]
		except:
			data = [{"Exception":"This Employee is Not prsent"}]

		return HttpResponse(data,content_type = "application/json")



	def post(self,request,question_id):
	
		try:
			t = Employee.objects.get(id=question_id)
			Name = request.POST.get('name','')
			Company = request.POST.get('company','')
			Category = request.POST.get('category','')
			t = Employee.objects.get(id=question_id)
			t.name = Name
			t.companyName = Company
			t.category = Category
			t.save()
			updated_emp = Employee.objects.get(id=question_id)
			data = serializers.serialize('json',[updated_emp])
		except:

			data = [{"Exception":"Person of this id is not prsent"}]

		return HttpResponse(data,content_type="application/json")

class HometemplateView(TemplateView):
	"""
		this is example for class based view
	"""

	template_name = "Audiences/detail.html"