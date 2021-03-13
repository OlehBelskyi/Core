from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('Core.auth_api.urls')),
    path('admin/', admin.site.urls),
]
