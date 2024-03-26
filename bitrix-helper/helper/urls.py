from django.urls import path
from .views import index, POSTLoginView, fiz, ur ,app_datail_fiz,app_datail_ur
from django.contrib.auth.views import LogoutView

app_name = 'helper'

urlpatterns = [
    path('', index, name='index'),
    path('login/', POSTLoginView.as_view(), name='login'),
    path('fiz/', fiz, name='fiz'),
    path('ur/', ur, name='ur'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('fiz/<int:pk>/', app_datail_fiz, name='app_datail_fiz'),
    path('ur/<int:pk>/', app_datail_ur, name='app_datail_ur'),

]
