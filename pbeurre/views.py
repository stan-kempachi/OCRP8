from django.db.models import Q
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.html import format_html
from .forms import LoginForm, RegisterForm, SearchForm
import logging, json

# personal import
from .models import Food, Category, Contact, Backup

logging.debug(__name__)

def index(request):
    form = SearchForm(request.POST)
    context = {
        'form': form
    }
    return render(request, 'pbeurre/index.html', context)


def mention_legale(request):
    return render(request,'pbeurre/mentionlegal.html')


def search(request):
    if request.GET:
        page = request.GET.get('page')
        query = request.GET.get('query')
        food = Food.objects.filter(name__icontains=query)[:1]
        substitute_list = Food.objects.filter(name__icontains=query).all().order_by('nutri_score')
        paginator = Paginator(substitute_list, 12)
        try:
            substitute = paginator.page(page)
        except PageNotAnInteger:
            substitute = paginator.page(1)
        except EmptyPage:
            substitute = paginator.page(paginator.num_pages)
        context = {
            'foods': food,
            'substitute': substitute,
            'paginate': True,
        }
        return render(request, 'pbeurre/search.html', context)


def details(request, food_id):
    form = SearchForm(request.POST)
    food = Food.objects.get(id=food_id)
    context = {
        'food': food,
        'form': form
    }
    return render(request, 'pbeurre/details.html', context)
