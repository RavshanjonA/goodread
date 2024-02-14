from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path

from config.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home"),
    path('user/', include("users.urls")),
    path('books/', include("users.books")),
]
