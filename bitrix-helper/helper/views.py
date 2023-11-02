from django.shortcuts import render, get_object_or_404, redirect
from .models import Application, AdvUser
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ApplicationForm, ChangeUserInfoForm, RegisterUserForm
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.signing import BadSignature
from .utilities import signer


@login_required
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
    return render(request, 'helper/index.html', {'Application': Application, 'form': form})


class POSTLoginView(LoginView):
    template_name = 'helper/login.html'


class POSTLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'helper/logout.html'


class POSTChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'helper/password_change.html'
    success_url = reverse_lazy('helper:profile')
    success_message = 'Password changed'



class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'helper/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('helper:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'helper/register_done.html'


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'helper/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'helper/user_is_activated.html'
    else:
        template = 'helper/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)
