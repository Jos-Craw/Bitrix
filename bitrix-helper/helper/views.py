from django.shortcuts import render, get_object_or_404, redirect
from .models import Application, AdvUser, PriceList
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegisterUserForm
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.signing import BadSignature


def index(request):
    Applications = Application.objects.filter(participants=request.user.id)
    PriceLists = PriceList.objects.filter(department=request.user.department)
    # добавить возможность добавления и удаления пункта прайс-листа в/из заявки
    return render(request, 'helper/index.html', {'Applications': Applications,'PriceLists':PriceLists})


class POSTLoginView(LoginView):
    template_name = 'helper/login.html'



class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'helper/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('helper:index')
