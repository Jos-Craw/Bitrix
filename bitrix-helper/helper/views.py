from django.shortcuts import render, get_object_or_404, redirect
from .models import Application, AdvUser
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ApplicationForm, RegisterUserForm
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.signing import BadSignature


def index(request):
    Applications = Application.objects.all()
    return render(request, 'helper/index.html', {'Applications': Applications})

    initial = {'Application': Application.pk}
    initial['author'] = request.user.username
    form = form_class(initial=initial)
    if request.method == 'POST':
        c_form = form_class(request.POST)
        if c_form.is_valid():
            c_form.save()
        else:
            form = c_form
    return render(request, 'helper/index.html', {'Applications': Applications, 'form': form})


class POSTLoginView(LoginView):
    template_name = 'helper/login.html'


class POSTLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'helper/index.html'



class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'helper/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('helper:index')
