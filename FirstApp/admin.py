from django.contrib import admin

from FirstApp.models import Topic, WebPage, AccessRecord, UserInfo

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(Topic)
admin.site.register(UserInfo)