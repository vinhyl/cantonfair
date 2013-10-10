from django.views.generic import TemplateView
from .models import Category, Product


class ProductView(TemplateView):
    template_name = "products\product.html"

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        context["product_list"] = Product.objects.all()
        return context
