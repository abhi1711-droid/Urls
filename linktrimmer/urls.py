from django.contrib import admin
from django.urls import path, include

from users.views import root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('<str:short_link>/', root, name='root'),
]
