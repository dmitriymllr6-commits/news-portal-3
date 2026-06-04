from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('news_app2.urls')),
    path('admin/', admin.site.urls),
]