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
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['search']
            foods = Food.objects.filter(Q(name__icontains=query))[:1]
            sub_foods = Food.objects.filter(Q(name__icontains=query))[:12]


        else:
            print("erreur 1")
            query = "Nutella"
            foods = Food.objects.filter(Q(name__icontains=query))[:1]
            sub_foods = Food.objects.filter(Q(name__icontains=query))
                                            # & Q(nutri_score='a') |
                                            # Q(name__icontains=query)
                                            # & Q(nutri_score='b'))[:6]
    else:
        print("erreur 2")
        return render(request, 'pbeurre/index.html')

    return render(request, 'pbeurre/search.html', {'foods':foods,
                                                   'substitute': sub_foods,
                                                   'form': form})


def details(request):
    query = "velouté"
    foods = Food.objects.filter(Q(name__icontains=query))[:1]
    return render(request,'pbeurre/details.html',{'foods':foods })


# def listing(request):
#     foods = Food.objects.filter(nutri_score=("a" or "b"or "c")).order_by('name')[:12]
#     formatted_foods = ["<li>{}</li>".format(food.name) for food in foods]
#     return HttpResponse(formatted_foods)


# def search(request):
#     form = SearchForm(request.POST)
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#
#         if form.is_valid():
#             query = form.cleaned_data['search']
#
#             foods = Food.objects.filter(Q(name__icontains=query)
#                                        & Q(nutri_score='e') |
#                                        Q(name__icontains=query) &
#                                        Q(nutri_score='d'))[:1]
#             """substitute method"""
            # if foods:
            #     sub_food = Food.objects.filter(Q(name__icontains=query)
            #                                           & Q(nutri_score='a') |
            #                                           Q(name__icontains=query)
            #                                           & Q(nutri_score='b'))[:6]
            #     if request.user.is_authenticated():
            #         user = request.user
            #         favori = Food.objects.filter(favourite__user_id=user.id)
            #         print(favori)
            #     else:
            #         favori = []
            # else:
            #     sub_food = []
            #     favori = []

    #     else:
    #         return redirect('/')
    # else:
    #     return redirect('/')
    #
    # return render(request, 'pbeurre/search.html', {'food': foods,
    #                                                       'form': form})




