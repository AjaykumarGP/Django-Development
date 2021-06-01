from django.urls import path
from FirstApp.views import testView, index, helpView


urlpatterns = [
    path('', helpView),
]