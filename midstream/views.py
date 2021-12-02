from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages

from midstream.forms import *


# Create your views here.
def create(request):
  template_name = 'midstream/midstream_form.html'

  # basic use permissions 基本使用權限; 添加這個但是在無痕中會出現404
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404

  form = MidstreamForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    instance = form.save(commit=False)
    # print(form.cleaned_data)
    instance.save()
    messages.success(request, "Success Created!!!")
    return HttpResponseRedirect(instance.get_absolute_url())
  else:
    messages.error(request,
                     "'NOT Successfully Save' + '<a href=''> NOT ITEM </a>' + 'Saved!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'",
                     extra_tags='html_safe'
                     )
  context = {
    'form': form,
    'title': 'Create Form',
  }
  return render(request, template_name, context)


def detail(request, id=None):
  # ins = Midstream.objects.get(id=id)
  instance = get_object_or_404(Midstream, id=id)
  context = {
    # 'ins': ins,
    'instance': instance,
    'title': 'instance.title'
  }
  return render(request, 'midstream/midstream_detail.html', context)
  # return HttpResponse('<h1>detail</h1>')


def list(request):
  # queryset_list = Midstream.objects.all()  # .order_by('-id')
  if request.user.is_staff or request.user.is_superuser:
    queryset_list = Midstream.objects.all()
    # if request.user.is_authenticated:
    #   context = {
    #     'obj_list': queryset,
    #     'title': '中游公司',
    #   }

    # else:
    #   context = {
    #     'title': 'Title',
    #   }

  # search
  query = request.GET.get("q")
  if query:
    queryset_list = queryset_list.filter(
      Q(store_name__icontains=query) |
      Q(store_holder__icontains=query) |
      Q(store_phoneNumber__icontains=query) |
      Q(store_address__icontains=query) |
      Q(store_email__icontains=query) |
      Q(store_notes__icontains=query)
    ).distinct()

  # paginator
  paginator = Paginator(queryset_list, 3)  # Show 25 contacts per page.
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

  context = {
    'page_request_var': page_request_var,
    'page_obj': page_obj,
    'obj_list': queryset,
    'title': '中游公司',
  }
  return render(request, 'midstream/midstream_list.html', context)
  # return HttpResponse('<h1>list</h1>')


def update(request, id=None):
  # basic use permissions 基本使用權限
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404

  instance = get_object_or_404(Midstream, id=id)
  form = MidstreamForm(request.POST or None, request.FILES or None, instance=instance)

  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    # message success
    messages.success(request,
                     "Successfully Save <a href='#'>ITEM </a> Saved!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
                     # "<div class="html_safe alert alert-success success" role="alert"><a href="#">Item</a> Saved</div>", #https://stackoverflow.com/questions/36899488/altering-the-default-django-messages-tag
                     extra_tags='html_safe'
                     )
    return HttpResponseRedirect(instance.get_absolute_url())
  else:
    messages.error(request, "Not successfully Created")
  context = {
    'form': form,
    'instance': instance,
    'title': 'EDIT',
  }
  return render(request, 'midstream/midstream_form.html', context)
  # return HttpResponse('<h1>update</h1>')


def delete(request, id=None):
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404

  instance = get_object_or_404(Midstream, id=id)
  instance.delete()
  messages.success(request, "SuccessFully Deleted!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
  return redirect("midstream:list")
  # return HttpResponse('<h1>update</h1>')

# def list(request):
#   ms_person = Midstream_person.objects.get()
#   ms_person_search = ms_person.books.all() # 取得查詢之作者(負責人)下的所有書籍(中游商公司有哪幾家)
#   context = {
#     'ms_person_search': ms_person_search,
#     'title': 'contact us',
#   }
#   return render(request, 'midstream/midstream_list.html', context)
