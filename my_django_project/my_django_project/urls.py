
from django.contrib import admin
from django.urls import include, path
import debug_toolbar

urlpatterns = [
    path('BaseApp/', include('BaseApp.urls')),
    path('', include('BaseApp.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]
