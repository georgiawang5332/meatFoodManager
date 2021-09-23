from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    print("Errors", form.errors)
    if form.is_valid():
      form.save()
      return redirect('')
    else:
      return render(request, 'registration/register.html', {'form': form})
  else:
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def profile(request):
  context = {
    'user': request.user,
    'title': 'profile',
  }
  # return HttpResponse('<h1>profile my info</h1>')
  return render(request, 'home/profile.html', context)


def home(request):
  context = {
    'title': 'home',
  }
  # return HttpResponse('<h1>home</h1>')
  return render(request, 'home/home.html', context)

# def HomeView(request):
#   return HttpResponse('<h1>home</h1>')

def contact(request):
  context = {
    'title': 'contact us',
  }
  # return HttpResponse('<h1>contact us</h1>')
  return render(request, 'home/contact.html', context)
