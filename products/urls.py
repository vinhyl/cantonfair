from django.conf.urls import patterns, url
from .views import ProductView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', ProductView.as_view()),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
