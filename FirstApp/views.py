from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Post, UserInfo
from . import forms
# from forms import BasicForm
# Create your views here.

#CRUD operations
#Listing all the posts here
def postListView(request):
	postObjects = Post.objects.all()
	context = {
		"postObjects" : postObjects
	}
	#render(request, "html", front transition data in dict)
	return render(request, "FirstApp/index.html", context)

def testView(request):
	return HttpResponse("Hello there!")

def helpView(request):
	sampleDict = {"Help": "How may I help you?"}
	return render(request, "FirstApp/helpPage.html", context = sampleDict)

def index(request):
	sampleDict = {"insertHere" : "Hello, I'm from views.py and rendering to index.html in templates folder in root directory"}
	return render(request, "FirstApp/index.html", context = sampleDict)	

def displayUserInfo(request):

	userInfo = UserInfo.objects.all()
	userDict = {
		"allData" : userInfo
	}
	return render(request, "FirstApp/userInfo.html", context = userDict)

def viewBasicForm(request):
	form = forms.BasicForm()

	if request.method == "POST":

		form = forms.BasicForm(request.POST)

		if form.is_valid():
			#Write the code here after getting data from the user(html page)
			#First clean the data
			print("Validation success")
			print("Name:" + form.cleaned_data['name'])
			print("Email:" + form.cleaned_data['email'])
			print("Text:" + form.cleaned_data['text'])

	return render(request, "FirstApp/basicForm.html", context = {
		"form" : form
		})

def viewStudentInfoForm(request):
	form = forms.StudentInfoForm()

	if request.method == "POST":
		form = forms.StudentInfoForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, "Data has been stored successfully")
			return redirect('/FirstApp/studentinfo')

	return render(request, 'FirstApp/studentInfo.html', context = {"form":form})



def other(request):
	return render(request, "FirstApp/other.html")

def relativeURL(request):
	return render(request, "FirstApp/relativeURL.html")