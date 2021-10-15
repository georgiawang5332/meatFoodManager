from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from home.models import *
from home.forms import *

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
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


@login_required
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

@login_required()
def home(request):
  form = HomeForm(request.POST)
  if form.is_valid():
    post = form.save(commit=False)
    post.user = request.user
    post.save()

    text = form.cleaned_data['user']
    form = HomeForm()
    return redirect('home:home')
  context = {
    'form': form,
    'title': 'home',
  }
  return render(request, 'home/home.html', context)
  # return HttpResponse('<h1>home</h1>')


def contact(request):
  context = {
    'title': 'contact us',
  }
  return render(request, 'home/contact.html', context)
  # return HttpResponse('<h1>contact us</h1>')
