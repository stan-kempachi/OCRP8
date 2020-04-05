from django.contrib import admin


from .models import Backup, Food, Category
# Register your models here.


@admin.register(Backup)
class BackupAdmin(admin.ModelAdmin):
    model = Backup
    fieldsets = [
        (None, {'fields': [ 'food']})
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


class FoodCategoryInline(admin.TabularInline):
    model = Food.category.through
    extra = 1
    verbose_name = "Aliment"
    verbose_name_plural = "Aliments"



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [FoodCategoryInline]


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass

