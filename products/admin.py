from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("model", "category", "order")
    list_editable = ("order",)
    list_filter = ("category",)
    search_fields = ["model"]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
