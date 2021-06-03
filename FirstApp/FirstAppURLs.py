from django.urls import path
from FirstApp.views import testView, index, helpView, displayUserInfo, viewBasicForm


urlpatterns = [
    path('', helpView),
    path('info/', displayUserInfo),
    path('form/', viewBasicForm)
]