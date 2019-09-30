from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import LoginForm, RegisterForm, SearchForm
# personal import
from .models import Food, Category, Contact, Backup


def index(request):
    form = SearchForm(request.POST)
    return render(request, 'pbeurre/index.html', {'form': form})

def page_not_found(request):
    """define error page"""
    return render(request, 'pbeurre/500.html')


def mention_legale(request):
    return render(request,'pbeurre/mentionlegal.html')


def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        if not query:
            return render(request, 'pbeurre/500.html')
        else:
            food = Food.objects.filter(Q(name__icontains=query))[:1]
            sub_foods = Food.objects.filter(Q(name__icontains=query)
                                            & Q(nutri_score='a') |
                                            Q(name__icontains=query)
                                            & Q(nutri_score='b') |
                                            Q(name__icontains=query)
                                            & Q(nutri_score='c') |
                                            Q(name__icontains=query)
                                            & Q(nutri_score='d') |
                                            Q(name__icontains=query)
                                            & Q(nutri_score='e'))\
                .order_by('nutri_score')

        context = {
            'foods': food,
            'substitute': sub_foods
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


