
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('dictionary.urls')),
    path('', include('accounts.urls')),
    path('api/auth/password_reset/', include('django_rest_passwordreset.urls')),
    path('admin/', admin.site.urls),
]
