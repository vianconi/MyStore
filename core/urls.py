import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
