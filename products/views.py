from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Category, Product


class ProductView(ListView):
    template_name = "products\product.html"
    model = Product
    context_object_name = "product_list"

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


class CategoryView(ListView):
    template_name = "products\product.html"
    context_object_name = "product_list"

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context
