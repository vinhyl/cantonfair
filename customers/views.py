from django.views.generic import CreateView, ListView
from .models import Customer
from .forms import CustomerForm
from products.models import Category


class CustomerCreateView(CreateView):
    model = Customer
    success_url = "thanks"
    form_class = CustomerForm

    def get_context_data(self, **kwargs):
        context = super(CustomerCreateView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


class ThanksView(ListView):
    model = Customer
    template_name = "customers\\thanks.html"

    def get_context_data(self, **kwargs):
        context = super(ThanksView, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context
