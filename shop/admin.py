from django.contrib import admin

from .models import Category, Product, ProductShots, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ["id", "name", "url",]
    list_display_links = ("name",)
    prepopulated_fields = {"url": ("name",)}


class ReviewInLine(admin.TabularInline):
    """Отзывы на странице товара"""
    model = Reviews
    extra = 0
    readonly_fields = ("name", "email")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Товары"""
    list_display = ["id", "name", "price", "category", "stock", "available", "url", "created", "updated"]
    list_display_links = ("name",)
    list_filter = ["available", "created", "updated"]
    list_editable = ("price", "stock", "available")
    prepopulated_fields = {"url": ("name",)}
    search_fields = ("name", "category__name")
    inlines = [ReviewInLine]
    save_on_top = True
    save_as = True
    # fields = ("category", ("name", "url"), ("description", "image"), ("price", "stock"), "available")
    fieldsets = (
        (None, {
            "fields": (("name", "category"),)
        }),
        (None, {
            "fields": (("description", "image"),)
        }),
        (None, {
            "fields": (("price", "stock"),)
        }),
        ("Options", {
            "fields": (("url", "available"),)
        }),
    )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("name", "email", "parent", "product", "id")
    readonly_fields = ("name", "email")


@admin.register(ProductShots)
class ProductShotsAdmin(admin.ModelAdmin):
    """Дополнительные фото товара"""
    list_display = ("title", "product")
