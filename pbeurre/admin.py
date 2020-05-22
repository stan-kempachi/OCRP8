from django.contrib import admin
from django.contrib.auth.models import User

from .models import Backup, Food, Category


@admin.register(Backup)
class BackupAdmin(admin.ModelAdmin):
    model = Backup
    fieldsets = [
        (None, {'fields': ['food']})
        ]
    extra = 1


class BackupInline(admin.TabularInline):
    model = Backup
    fieldsets = [
        (None, {'fields': ['food']})
        ]
    extra = 1
    verbose_name = "Favori"
    verbose_name_plural = "Favoris"


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    model = Food
    fieldsets = [
        (None, {'fields': ['name',
                           'nutri_score',
                           'picture']})
    ]
    extra = 1


class FoodCategoryInline(admin.TabularInline):
    model = Food
    extra = 1
    verbose_name = "Aliment"
    verbose_name_plural = "Aliments"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fieldsets = [
        (None, {'fields': ['name',
                           'picture']})
        ]
    extra = 1


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1
    verbose_name = "Catégorie"
    verbose_name_plural = "Catégories"


