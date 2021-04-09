from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rpi_manager.views import home

urlpatterns = [
    path("", home.index, name="home"),
    path('admin/', admin.site.urls),
    path("rpi/", include("rpi_manager.urls")),
    path("user/", include("user.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns