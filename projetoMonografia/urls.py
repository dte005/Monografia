from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ordens/', include('ordensDeServico.urls')),
    path('admin/', admin.site.urls),
]
