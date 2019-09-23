from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .forms import LoginForm, RegisterForm, SearchForm
# personal import
from .models import Food, Category, Contact, Backup


def index(request):
    form = SearchForm(request.POST)
    return render(request, 'pbeurre/index.html', {'form': form})

def page_not_found(request):
    """define error page"""
    return render(request, 'pbeurre/404.html'), 404


def mention_legale(request):
    return render(request,'pbeurre/mentionlegal.html')


def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        if not query:
            foods = Food.objects.all()[:1]
            sub_foods = Food.objects.all()[:12]
            if not foods.exists():
                print("not food exists")
        else:
            foods = Food.objects.filter(Q(name__icontains=query))[:1]
            sub_foods = Food.objects.filter(Q(name__icontains=query))[:12]
        context = {
            'foods': foods,
            'substitute': sub_foods
        }
        return render(request, 'pbeurre/search.html', context)



def details(request, food_id):
    form = SearchForm(request.POST)
    food = Food.objects.get(id=food_id)
    return render(request, 'pbeurre/details.html',
                  {'food': food,
                   'form': form, })

# def search(request):
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             query = form.cleaned_data['search']
#             foods = Food.objects.filter(Q(name__icontains=query))[:1]
#             sub_foods = Food.objects.filter(Q(name__icontains=query))[:12]
#
#
#         else:
#             print("erreur 1")
#             query = "Nutella"
#             foods = Food.objects.filter(Q(name__icontains=query))[:1]
#             sub_foods = Food.objects.filter(Q(name__icontains=query))
#                                             # & Q(nutri_score='a') |
#                                             # Q(name__icontains=query)
#                                             # & Q(nutri_score='b'))[:6]
#     else:
#         print("erreur 2")
#         return render(request, 'pbeurre/index.html')
#
#     return render(request, 'pbeurre/search.html', {'foods':foods,
#                                                    'substitute': sub_foods,
#                                                    'form': form})


