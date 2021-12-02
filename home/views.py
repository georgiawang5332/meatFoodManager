from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from home.forms import *
from home.models import *
from midstream.models import *

from django.contrib.auth.decorators import login_required


# Create your views here.
def list(request):
  # queryset_list = Midstream.objects.all()  # .order_by('-id')
  if request.user.is_staff or request.user.is_superuser:
    queryset_list = Midstream.objects.all()

  context = {
    'obj_list': queryset_list,
    'title': '中游公司',
  }
  return render(request, 'midstream/midstream_list.html', context)
  # return HttpResponse('<h1>list</h1>')


def changePassword(request):
  if request.method == "POST":
    form = PasswordChangeForm(data=request.POST, user=request.user)
    if form.is_valid():
      form.save()
      return redirect('home:home')
  else:
    form = PasswordChangeForm(user=request.user)
    context = {
      'form': form,
    }
    return render(request, 'home/home.html', context)


def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    print("Errors", form.errors)
    if form.is_valid():
      form.save()
      return redirect('home')
    else:
      return render(request, 'registration/register.html', {'form': form})
  else:
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def profile(request):
  context = {
    'user': request.user,
    'title': 'profile',
  }
  return render(request, 'home/profile.html', context)
  # return HttpResponse('<h1>profile my info</h1>')


@login_required
def home(request):
  # current_event = Midstream.objects.lastest()
  # Entry.objects.latest('pub_date', '-expire_date')  #您還可以根據多個字段選擇最新的。例如，要在兩個條目相同時選擇Entry最早expire_date的 pub_date：

  current_event = Midstream.objects.order_by('-pk')[:3] #https://www.itread01.com/content/1549962732.html

  if request.user.is_staff or request.user.is_superuser:
    queryset_list = Midstream.objects.all()
  form = HomeForm(request.POST)
  if form.is_valid():
    post = form.save(commit=False)
    post.user = request.user
    post.save()

    text = form.cleaned_data['user']
    form = HomeForm()
    return redirect('home:home')
  context = {
    'obj_list': queryset_list,
    'title': '中游公司',
    'form': form,
    'current_event': current_event,
  }
  return render(request, 'home/home.html', context)


def contact(request):
  context = {
    'title': 'contact us',
  }
  return render(request, 'home/contact.html', context)
  # return HttpResponse('<h1>contact us</h1>')
