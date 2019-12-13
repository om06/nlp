"""nlp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve

from .converter import views as converter_views

urlpatterns = [
    # Admin urls
    # ------------------------------------------------------------------------------------------------------------------
    path('admin/', admin.site.urls),

    # Converter urls
    # ------------------------------------------------------------------------------------------------------------------
    url('^$', converter_views.home, name='home'),
    url('^transcription/delete/(?P<pk>\d+)$', converter_views.delete_transcription, name="delete_transcription")

]


# For accessing media and static files in the debug mode
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [url(r'^static/(?P<path>.*)$', serve)] + \
                   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
