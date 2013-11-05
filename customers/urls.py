from django.conf.urls import patterns, url
from .views import CustomerCreateView, ThanksView


urlpatterns = patterns('',
    url(r'^customer/$', CustomerCreateView.as_view(), name="customer"),
    url(r'^customer/thanks/$', ThanksView.as_view(), name="thanks"),
)
