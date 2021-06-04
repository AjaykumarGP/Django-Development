from django.urls import path
from FirstApp.views import viewStudentInfoForm, testView, index, helpView, displayUserInfo, viewBasicForm, relativeURL, other



app_name = "FirstApp"

urlpatterns = [
    path('', helpView),
    path('info/', displayUserInfo),
    path('form/', viewBasicForm),
    path('studentinfo/', viewStudentInfoForm),
    path('relative/', relativeURL, name = "relative"),
    path('other/', other, name = "other"),
]