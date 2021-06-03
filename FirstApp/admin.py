from django.contrib import admin

from FirstApp.models import Topic, WebPage, AccessRecord, UserInfo, StudentInfo, Post

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(Topic)
admin.site.register(UserInfo)
admin.site.register(StudentInfo)
admin.site.register(Post)