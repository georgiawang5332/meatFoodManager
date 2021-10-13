from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from mass_mer.forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import Http404

from mass_mer.models import *

# Create your views here.
def stdisplay(request):
  queryset_list = Mass_Mer.objects.all()

  context= {
    "crudst": queryset_list,
  }
  return render(request, "mass_mer/index.html", context)


def stinstert(request):
  if request.method == "POST":
    if request.POST.get('mailbox') and request.POST.get('company_phone') and request.POST.get('address') and request.POST.get('uniform_numbers') and request.POST.get('regional_app_num'):# and request.POST.get('stgender'):
      savest = Mass_Mer()
      savest.mailbox = request.POST.get('mailbox')
      savest.company_phone = request.POST.get('company_phone')
      savest.address = request.POST.get('address')
      savest.uniform_numbers = request.POST.get('uniform_numbers')
      savest.regional_app_num = request.POST.get('regional_app_num')
      savest.save()
      messages.success(request, "The Record" + savest.company_name + "Is Saved Successfully....!")
      return render(request, "mass_mer/massmerCreate.html")
  else:
    return render(request, "mass_mer/massmerCreate.html")

# /////////////////////////TEST/////////////////////////
def MassMerPersonList(request):  # 量販店 Display
  # results = Mass_Mer_Person.objects.all()
  queryset_list = Mass_Mer_Person.objects.active()
  if request.user.is_staff or render.user.is_authenticated:
    queryset_list = Mass_Mer_Person.objects.all()

  # search
  query = request.GET.get("q")
  if query:
      queryset_list = queryset_list.filter(
        Q(mass_mer_principal__icontains=query) |
        Q(certificate_num_principal__icontains=query) |
        Q(telephone__icontains=query) |
        Q(address__icontains=query)
      ).distinct()

  # paginator
  paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page.
  page_request_var = 'page'
  page_number = request.GET.get(page_request_var)

  try:
    queryset = paginator.page(page_number)
  except PageNotAnInteger:
    # if page is not an integer, deliver first page.
    queryset = paginator.page(1)
  except EmptyPage:
    queryset = paginator.page(paginator.num_pages)

  page_obj = paginator.get_page(page_number)

  context= {
    'page_request_var': page_request_var,
    'page_obj': page_obj,
    'obj_list': queryset,
  }

  return render(request, "mass_mer/index.html", context)


from django.http import HttpResponseRedirect
def MassMerPersonCreate(request):  # 量販店負責人 instert
  # if request.method == "POST":
  #   if request.POST.get('mass_mer_principal') and request.POST.get('certificate_num_principal') and request.POST.get('telephone') and request.POST.get('address'):
  #     savest                           = Mass_Mer_Person()
  #     savest.mass_mer_principal        = request.POST.get('mass_mer_principal')
  #     savest.certificate_num_principal = request.POST.get('certificate_num_principal')
  #     savest.telephone                 = request.POST.get('telephone')
  #     savest.address                   = request.POST.get('address')
  #     savest.save()
  #     messages.success(request, "The Record" + savest.mass_mer_principal + "Is Saved Successfully....!")
  #     return render(request, "mass_mer/massmerCreate.html")
  # else:
  #   return render(request, "mass_mer/massmerCreate.html")

  if not request.user.is_staff or not request.user.is_superuser:  # 基本用戶權限
    raise Http404
  form = stform(request.POST or None, request.FILES or None)
  if form.is_valid():
    instance = form.save(commit=False)
    print(form.cleaned_data)
    instance.save()
    # message success
    messages.success(request, "Successfully Created")
    return HttpResponseRedirect(instance.get_absolute_url())
  # else:
  #   messages.error(request, "Not successfully Created")
  context = {
    'form': form,
    'title': 'Create Store'
  }
  return render(request, "mass_mer/massmerCreate.html", context)

def MassMerPersonEdit(request, id=None):
  massmerpersonDetails = Mass_Mer_Person.objects.get(id=id)
  return render(request, "mass_mer/massmerEdit.html", {"crudst": massmerpersonDetails})

def MassMerPersonUpdate(request, id=None):
  if not request.user.is_staff or not request.user.is_superuser:  # 基本用戶權限
    raise Http404
  massmerpersonUpdate = Mass_Mer_Person.objects.get(id=id)
  # form = stform(request.POST, instance=massmerpersonUpdate)
  form = stform(request.POST or None, instance=massmerpersonUpdate)
  if form.is_valid():
    # form.save()
    instance = form.save(commit=False)
    print(form.cleaned_data)
    instance.save()
    # message success
    messages.success(request, "the xxx Record is Updated successfully... !")
  else:
    messages.error(request, "Not successfully Created")
  return render(request, "mass_mer/massmerEdit.html", {"crudst": massmerpersonUpdate, 'form': form})



def MassMerPersonDel(request, id=None):
  massmerpersonDel = Mass_Mer_Person.objects.get(id=id)
  massmerpersonDel.delete()
  results = Mass_Mer_Person.objects.all()
  return render(request, "mass_mer/index.html", {"crudst": results})

def MassMerPersonDetail(request, id=None):
  instance = get_object_or_404(Mass_Mer_Person, id=id)
  context = {
    'instance': instance,
    'title': 'instance.title'
  }
  return render(request, 'mass_mer/massmerDetail.html', context)
  # return HttpResponse('<h1>detail</h1>')


def MassMerList(request):  # 攤商
  return HttpResponse('<h1>MassMer List List</h1>')

def FoodVendorList(request):  # 攤商
  return HttpResponse('<h1>Food Vendor List</h1>')


def StorefrontList(request):  # 店面
  pass
  # results = Mass_Mer_Person.objects.all()
  # queryset_list = Mass_Mer_Person.objects.active()
  # if request.user.is_staff or render.user.is_authenticated:
  #   queryset_list = Mass_Mer_Person.objects.all()
  #
  # # search
  # query = request.GET.get("q")
  # if query:
  #   queryset_list = queryset_list.filter(
  #     Q(mass_mer_principal__icontains=query) |
  #     Q(certificate_num_principal__icontains=query) |
  #     Q(telephone__icontains=query) |
  #     Q(address__icontains=query)
  #   ).distinct()
  #
  # # paginator
  # paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page.
  # page_request_var = 'page'
  # page_number = request.GET.get(page_request_var)
  #
  # try:
  #   queryset = paginator.page(page_number)
  # except PageNotAnInteger:
  #   # if page is not an integer, deliver first page.
  #   queryset = paginator.page(1)
  # except EmptyPage:
  #   queryset = paginator.page(paginator.num_pages)
  #
  # page_obj = paginator.get_page(page_number)
  #
  # context = {
  #   'page_request_var': page_request_var,
  #   'page_obj': page_obj,
  #   'obj_list': queryset,
  # }

  # return render(request, "mass_mer/index.html", context)


def RetailFactoryList(request):  # 零售業(工廠)
  return HttpResponse('<h1>Retail Factory List</h1>')


def OtherList(request):  # 其他
  return HttpResponse('<h1>Other List</h1>')
