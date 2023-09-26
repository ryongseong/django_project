from django.contrib import admin
from django.urls import path, include
from insight.views import index, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('insight/', include('insight.urls')),
    path('result/', include('insight.urls')),
]
