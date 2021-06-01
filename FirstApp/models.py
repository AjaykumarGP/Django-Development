from django.db import models

#creating a new model, which represent a single table in the database
class Post(models.Model):

	#fields od the model
	title = models.CharField(max_length = 120)
	descriptions = models.TextField()

	def __str__(self):
		return self.title
