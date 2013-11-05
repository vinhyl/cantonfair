from django.conf.urls import patterns, url
from .views import ProductView, CategoryView, AboutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^about/$', AboutView.as_view(), name="about"),
    url(r'^(?P<slug>[\w-]+)/$', CategoryView.as_view(), name="category"),
    url(r'^$', ProductView.as_view())
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
