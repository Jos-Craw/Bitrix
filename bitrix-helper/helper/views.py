from django.shortcuts import render, get_object_or_404, redirect
from .models import Applicationf, Applicationu, AdvUser, PriceListFiz, PriceListUr, Department
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.signing import BadSignature
from docxtpl import DocxTemplate

def index(request):
    return render(request, 'helper/index.html')


class POSTLoginView(LoginView):
    template_name = 'helper/login.html'


def fiz(request):
    Applicationsf = Applicationf.objects.filter(participants=request.user.id)
    if request.user.is_authenticated:
        PriceListsf = PriceListFiz.objects.filter(department=request.user.department)
        cont = {'Applicationsf': Applicationsf,'PriceListsf':PriceListsf}
    else: cont = {'Applicationsf': Applicationsf}
    return render(request, 'helper/fiz.html',cont)

def ur(request):
    Applicationsu = Applicationu.objects.filter(participants=request.user.id)
    if request.user.is_authenticated:
        PriceListsu = PriceListUr.objects.filter(department=request.user.department)
        cont = {'Applicationsu': Applicationsu,'PriceListsu':PriceListsu}
    else: cont = {'Applicationsu': Applicationsu,}
    return render(request, 'helper/ur.html',cont)

def app_datail_fiz(request, pk):
    Applicationsf = Applicationf.objects.filter(participants=request.user.id)
    app_f = get_object_or_404(Applicationsf, pk=pk)
    PriceListsf = PriceListFiz.objects.filter(department=request.user.department)
    if request.POST.get('delete'):
        price_id = request.POST.get('item_id')
        app_f.pricelistFiz.remove(list(PriceListsf)[int(price_id)-1])
    if request.POST.get('add'):
        price_id = request.POST.get('item_id')
        app_f.pricelistFiz.add(list(PriceListsf)[int(price_id)-1])
    if request.POST.get('create_doc'):
        doc = DocxTemplate("helper/price.docx")
        doc.render({'a': str(list(PriceListsf)[1])}) #отредактироваить вывод и вообще его сделать
        doc.save('helper/p1.docx')
    return render(request, 'helper/app_detail_fiz.html', {'app_f': app_f,'PriceListsf':PriceListsf})


def app_datail_ur(request, pk):
    Applicationsu = Applicationu.objects.filter(participants=request.user.id)
    app_u = get_object_or_404(Applicationsu, pk=pk)
    PriceListsu = PriceListUr.objects.filter(department=request.user.department)
    if request.POST.get('delete'):
        price_id = request.POST.get('item_id')
        app_u.pricelistUr.remove(list(PriceListsu)[int(price_id)-1])
    if request.POST.get('add'):
        price_id = request.POST.get('item_id')
        app_u.pricelistUr.add(list(PriceListsu)[int(price_id)-1])
    if request.POST.get('create_doc'):
        doc = DocxTemplate("helper/price.docx")
        doc.render({'a': str(list(PriceListsf)[1])}) #отредактироваить вывод и вообще его сделать
        doc.save('helper/p2.docx')
    return render(request, 'helper/app_detail_ur.html', {'app_u': app_u,'PriceListsu':PriceListsu})
