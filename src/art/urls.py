from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import (index, gallery, details, post_details, events, contact, about)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('gallery', gallery),
    path('details', details),
    path('events', events),
    path('contact', contact),
    path('about', about),
    path('post_details', post_details),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)