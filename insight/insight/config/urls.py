from django.contrib import admin
from django.urls import path, include
from insight.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('insight/', include('insight.urls')),
    path('result/', include('insight.urls')),
]
