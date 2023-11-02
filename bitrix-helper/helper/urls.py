from django.urls import path
from django.contrib.auth.views import LoginView
from .views import index, POSTLoginView, POSTLogoutView,POSTChangeView, RegisterUserView, RegisterDoneView, user_activate

app_name = 'helper'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/login/', POSTLoginView.as_view(), name='login'),
    path('accounts/logout/', POSTLogoutView.as_view(), name='logout'),
    path('accounts/password/change', POSTChangeView.as_view(), name='password_change'),

]
