from django.db import models
from django.contrib.auth.models import User

CHRFIELD_LEN = 200
TXTFIELD_LEN = 2000

PRODUCT_TYPE = (
    ("bread", "Bread"),
    ("cakes", "Cakes"),
    ("pies", "Pies"),
    ("muffins", "Muffins"),
    ("assorted_pastries", "Assorted Pastries"),
    ("savoury_items", "Savoury Items"),
)


class Product(models.Model):
    """
    Database model for a bakery product.
    """
    name = models.CharField(max_length=CHRFIELD_LEN, blank=True, null=True)
    description = models.CharField(max_length=TXTFIELD_LEN, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=200, choices=PRODUCT_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='main_site')

    def __str__(self):
        return self.name
