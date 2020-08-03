from django.contrib import admin

from .models import Category, Product, ProductShots, Reviews

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductShots)
admin.site.register(Reviews)
