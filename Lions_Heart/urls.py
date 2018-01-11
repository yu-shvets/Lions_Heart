"""Lions_Heart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [

    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^', include('lions_heart_products.urls')),
    url(r'^blog', include('lions_heart_blog.urls')),
    url(r'^', include('lions_heart_cart.urls')),
    # url(r'^', include('lions_heart_billing.urls')),

    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(url(r'^', include('lions_heart_products.urls')))

if settings.DEBUG:
        import debug_toolbar
        urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls))] + urlpatterns
