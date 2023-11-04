from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import index, POSTLoginView, POSTLogoutView, RegisterUserView, POSTLogoutView

app_name = 'helper'

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', POSTLoginView.as_view(), name='login'),
    path('logout/',POSTLogoutView.as_view(next_page=''), name='logout'),

]
