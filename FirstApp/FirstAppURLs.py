from django.urls import path
from FirstApp.views import testView


urlpatterns = [
    path('', testView),
]