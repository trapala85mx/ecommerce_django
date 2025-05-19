from django.http import HttpRequest
from django.shortcuts import render

from .models import Categorie, Product


# Create your views here.
# VISTA PARA CATÁLOGO DE PRODUCTOS
def index(request):
    """Vista para index"""
    products = Product.objects.all()
    categories = Categorie.objects.all()
    context = {
        "products": products,
        "categories": categories,
    }
    return render(request, "index.html", context=context)


def productos_por_categoria(request, categoria_id: int):
    """Vista para mostrar los productos por categoría."""
    category_ob = Categorie.objects.get(pk=categoria_id)
    products_category = category_ob.product_set.all()

    categories = Categorie.objects.all()

    context = {
        "products": products_category,
        "categories": categories,
    }

    return render(request, "index.html", context=context)


def barra_busqueda(request: HttpRequest):
    """Vista para la barra de búsqueda"""
    nombre = request.POST["nombre"]
    print(nombre)
    products = Product.objects.filter(name__icontains=nombre)
    print(products)
    categories = Categorie.objects.all()

    context = {
        "products": products,
        "categories": categories,
    }

    return render(request, "index.html", context)


# VISTAS PARA EL CARRITO DE COMPRAS
def carrito(request):
    """Vista para el carrito de compras"""
    return (request, "carrito.html")
