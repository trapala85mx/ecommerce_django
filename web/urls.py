from django.urls import path

from .views import index, productos_por_categoria

app_name = "web"

urlpatterns = [
    path("", view=index),
    path(
        "productos-por-categoria/<int:categoria_id>/",
        view=productos_por_categoria,
        name="productos_categoria",
    ),
]
