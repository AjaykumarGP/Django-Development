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
	return render(request, "Posts/index.html", context)

def testView(request):
	return HttpResponse("Hello there!")