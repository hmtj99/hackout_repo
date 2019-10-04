from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("hospitals.urls", namespace="hospitals"),),
    path('donors/', include("donors.urls", namespace="donors"),)
]
