from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rpi_manager.views import index

urlpatterns = [
    path("", index.index, name="index"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns