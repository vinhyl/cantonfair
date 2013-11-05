from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import Category, Product


class AboutView(TemplateView):
    template_name = "products\\about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


class DemoView(TemplateView):
    template_name = "products\milkfrother.html"

    def get_context_data(self, **kwargs):
        context = super(DemoView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


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
