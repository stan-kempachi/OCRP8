from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# personal import
from .models import Food, Backup
from .forms import RegisterForm, SearchForm, LoginForm


key = '4bf8zx8t^se760vf#$sm^p_%j=*i=nccqjb#kp(2ug+6e51_(*'


def index(request):
    form = SearchForm(request.POST)
    context = {
        'form': form
    }
    return render(request, 'pbeurre/index.html', context)


def search(request, ):
    if request.GET:
        user = request.user
        query = request.GET.get('q')
        food = Food.objects.filter(name__icontains=query)[:1]
        foo = get_object_or_404(food)
        substitute_list = []
        if foo.nutri_score == 'a':
            substitute_list = Food.objects.filter(Q(name__icontains=query) & Q
                                                   (category_tags2__icontains=foo.category) & Q
                                                   (nutri_score__lte=foo.nutri_score))

        if foo.nutri_score == 'b':
            substitute_list = Food.objects.filter(Q(name__icontains=query) & Q
                                                   (category_tags2__icontains=foo.category) & Q
                                                   (nutri_score__lte=foo.nutri_score))

        if foo.nutri_score == 'c':
            substitute_list = Food.objects.filter(Q(name__icontains=query) & Q
                                                   (category_tags2__icontains=foo.category) & Q
                                                   (nutri_score__lt=foo.nutri_score))
        if foo.nutri_score == 'd':
            substitute_list = Food.objects.filter(Q(name__icontains=query) & Q
                                                   (category_tags2__icontains=foo.category) & Q
                                                   (nutri_score__lt=foo.nutri_score))
        if foo.nutri_score == 'e':
            substitute_list = Food.objects.filter(Q(name__icontains=query) & Q
                                                   (category_tags2__icontains=foo.category) & Q
                                                   (nutri_score__lt=foo.nutri_score))
        if len(substitute_list) == 0:
            try:
                substitute_list = Food.objects.filter(Q(category_tags2__icontains=foo.category) & Q
                                                       (nutri_score__lt=foo.nutri_score))
            except:
                pass
        substitute_list = substitute_list.order_by('nutri_score')
        substitute_list = substitute_list.exclude(name=foo.name)
        favori = Food.objects.filter(Q(backup__user_id=user.id))

        # paginator settings
        page = request.GET.get('page')
        paginator = Paginator(substitute_list, 6)
        try:
            substitute = paginator.page(page)
        except PageNotAnInteger:
            substitute = paginator.page(1)
        except EmptyPage:
            substitute = paginator.page(paginator.num_pages)
        context = {
            'favori': favori,
            'foods': food,
            'substitute': substitute,
            'paginate': True,
        }
        return render(request, 'pbeurre/search.html', context)
    else:
        return render(request, 'pbeurre/index.html')


def details(request, food_id):
    form = SearchForm(request.POST)
    food = get_object_or_404(Food, id=food_id)
    context = {
        'food': food,
        'form': form
    }
    return render(request, 'pbeurre/details.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'pbeurre/index.html')
            else:
                messages.error(request, "Identifiants invalides")
                return render(request, 'pbeurre/login.html', {'form': form})
    return render(request, 'pbeurre/login.html')


def mention_legale(request):
    return render(request, 'pbeurre/mentionlegal.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if User.objects.filter(email=email).exists():
                messages.error(request, "Cette adresse email existe déjà.")
                return render(request, 'pbeurre/register.html')
            else:
                user = User.objects.create_user(password=password,
                                                email=email,
                                                username=name)
                login(request, user)
                return render(request, 'pbeurre/index.html')
        else:
            return redirect('pbeurre:register')
    else:
        form = RegisterForm()
    return render(request, 'pbeurre/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.error(request, "Vous êtes déconnecté")
    return render(request, 'pbeurre/index.html')


@login_required()
def mon_compte(request):
    user = request.user
    user = User.objects.filter(email=user.email).get()
    context = {
        'user': user}
    return render(request, 'pbeurre/mon_compte.html', context)


@login_required()
def add_favorite(request, food_id):
    user = request.user
    food = Food.objects.get(id=food_id)
    backup = Food.objects.filter(backup__user_id=user.id).order_by('nutri_score')
    save = Backup.objects.filter(user=user)
    if save:
        add = Backup.objects.get(user_id=user.id)
        add.food.add(food)
    else:
        add = Backup.objects.create(user_id=user.id)
        add.food.add(food)
    # paginator settings
    page = request.GET.get('page')
    paginator = Paginator(backup, 9)
    try:
        favoris = paginator.page(page)
    except PageNotAnInteger:
        favoris = paginator.page(1)
    except EmptyPage:
        favoris = paginator.page(paginator.num_pages)
    context = {
        'favori': backup,
        'paginate': True,
        'favoris': favoris
    }
    return render(request, 'pbeurre/favorite.html', context)


@login_required()
def favorite(request):
    user = request.user
    backup = Food.objects.filter(backup__user_id=user.id).order_by('nutri_score')
    # paginator settings
    page = request.GET.get('page')
    paginator = Paginator(backup, 9)
    try:
        favoris = paginator.page(page)
    except PageNotAnInteger:
        favoris = paginator.page(1)
    except EmptyPage:
        favoris = paginator.page(paginator.num_pages)
    context = {
        'favori': backup,
        'paginate': True,
        'favoris': favoris
    }
    return render(request, 'pbeurre/favorite.html', context)


@login_required()
def remove_favorite(request, food_id):
    user = request.user
    rem = Food.objects.filter(backup__user_id=user.id)
    rm = rem.get(id=food_id)
    rm.delete()
    backup = Food.objects.filter(
        backup__user_id=user.id
    ).order_by('nutri_score')
    # paginator settings
    page = request.GET.get('page')
    paginator = Paginator(backup, 9)
    try:
        favoris = paginator.page(page)
    except PageNotAnInteger:
        favoris = paginator.page(1)
    except EmptyPage:
        favoris = paginator.page(paginator.num_pages)
    context = {
        'favori': backup,
        'paginate': True,
        'favoris': favoris
    }
    return render(request, 'pbeurre/favorite.html', context)
