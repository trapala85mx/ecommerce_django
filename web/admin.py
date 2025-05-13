"""web/admin.py"""

from django.contrib import admin

from .models import Categorie, Product

# Register your models here.
admin.site.register(Categorie)
# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Clase para registrar de manera personalizada
    el Modelo Product dentro del Admin de Django.
    """

    # campos que se mostrarán en el admin en la
    # sección de productos
    list_display = ["name", "price", "category"]
    # campos que se podrán modificar dentro de la
    # sección de productos
    list_editable = ["price"]
