
## Introduction

> -  Projet réalisé par moi-même étudiant chez Openclassrooms
> - Plateforme permettant de comparer des produits alimentaires selon leurs nutri-score, de mieux consommer.
> - Date de fin: Juin 2020
> - Démo en ligne : http://134.209.31.48/
> - Language : Python-Django, HTML, CSS, architecture MVT (model-vue-template)


## Code Samples

>     if request.GET:
        user = request.user
        query = request.GET.get('q')
        food = Food.objects.filter(name__icontains=query)[:1]
        foo = get_object_or_404(food)
        substitute_list = []
        if foo.nutri_score == 'a':
            substitute_list = Food.objects.filter(Q(name__icontains=query) & Q
                                                   (category_tags2__icontains=foo.category) & Q
                                                   (nutri_score__lte=foo.nutri_score))

## Installation

> - Telecharger le projet
> - Rendez-vous dans le dossier
> - Créez un environnement virtuel pour python avec virtualenv (!!! peut-être que vous devrez installer virtualenv !!!)
> - Activer l'environnement virtuel
> - Installer les dépendances avec Pip (!!! peut-être que vous devrez installer Pip !!!)
> - Exécuter python manage.py runserver
> - Ouvre votre navigateur et saisissez cette adresse: http://127.0.0.1:8000/
> - Enjoy ;D !




    
