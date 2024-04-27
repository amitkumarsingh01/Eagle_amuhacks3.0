from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('utils/', include('utils.urls')),
    path('', include('dashboard.urls')),
    path('predict/', include('predict.urls')),
]
