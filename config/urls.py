
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from config.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home"),
    path('user/', include("apps.users.urls")),
    path('books/', include("apps.books.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)