from django.db import models

#creating a new model, which represent a single table in the database
class Post(models.Model):

	#fields od the model
	title = models.CharField(max_length = 120)
	descriptions = models.TextField()

	def __str__(self):
		return self.title

class Topic(models.Model):
	
	topicName = models.CharField(max_length=264, unique = True)

	def __str__(self):
		return self.topicName

class WebPage(models.Model):
	
	topic = models.ForeignKey("Topic", on_delete=models.PROTECT)
	name = models.CharField(max_length=264, unique=True)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.name

class AccessRecord(models.Model):

	name = models.ForeignKey("WebPage", on_delete=models.PROTECT)
	date = models.DateField()

	def __str__(self):
		return str(self.date)
		

class UserInfo(models.Model):

	firstName = models.CharField(max_length = 100)
	lastName = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)

	def __str__(self):
		return self.email


#student info model
class StudentInfo(models.Model):
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	course = models.CharField(max_length=100)

	def __str__(self):
		return self.firstName

