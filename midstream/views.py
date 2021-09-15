from django.shortcuts import render
from .models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse


# Create your views here.
def list(request):
  # ms_person = Midstream_person.objects.get(name=company_person)
  # ms_person_search = ms_person.books.all()
  # 取得查詢之作者(負責人)下的所有書籍(中游商公司有哪幾家)
  context = {
    # 'ms_person_search': ms_person_search,
    'title': 'contact us',
  }
  return render(request, 'midstream/midstream_list.html', context)
  # return HttpResponse('<h1>Midstream_person</h1>')

