from django.urls import path
from FirstApp.views import viewStudentInfoForm, testView, index, helpView, displayUserInfo, viewBasicForm


urlpatterns = [
    path('', helpView),
    path('info/', displayUserInfo),
    path('form/', viewBasicForm),
    path('studentinfo/', viewStudentInfoForm)
]