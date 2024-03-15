from django.urls import path
from .views import index, POSTLoginView, RegisterUserView, fiz, ur
from django.contrib.auth.views import LogoutView

app_name = 'helper'

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', POSTLoginView.as_view(), name='login'),
    path('fiz/', fiz, name='fiz'),
    path('ur/', ur, name='ur'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
