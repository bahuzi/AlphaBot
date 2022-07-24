from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('alphabot/', include('alphabot.urls')),
    path('admin/', admin.site.urls),
]