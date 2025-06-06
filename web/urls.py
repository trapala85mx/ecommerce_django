from django.urls import path

from .views import barra_busqueda, detalle_producto, index, productos_por_categoria

app_name = "web"

urlpatterns = [
    path("", view=index),
    path(
        "productos-por-categoria/<int:categoria_id>/",
        view=productos_por_categoria,
        name="productos_categoria",
    ),
    path("buscar-producto/", view=barra_busqueda, name="barra_busqueda"),
    path("producto/<int:producto_id>/", view=detalle_producto, name="detalle_producto"),
]
