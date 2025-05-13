"""web/models.py"""

from django.db import models


# Create your models here.
class Categorie(models.Model):
    """
    Django Model to represent a category for a product.
    """

    name = models.CharField(
        max_length=100,
        verbose_name="nombre",
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última actualización",
    )

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    """
    Django Model to represent a Product.
    """

    category = models.ForeignKey(
        to=Categorie,
        on_delete=models.RESTRICT,
        verbose_name="Categoría",
    )
    name = models.CharField(max_length=100, verbose_name="Producto")
    description = models.TextField(verbose_name="Descripción", null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    image = models.ImageField(upload_to="productos/", verbose_name="Imagen")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última actualización",
    )

    def __str__(self):
        return f"{self.name}"
