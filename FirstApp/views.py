from django.shortcuts import render

from django.http import HttpResponse
from .models import Post
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