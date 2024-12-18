from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('main/')), # Redirect root URL to main/
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]
