
from django.contrib import admin

from apps.users.models import User, BookShelf

admin.site.register([User, BookShelf])