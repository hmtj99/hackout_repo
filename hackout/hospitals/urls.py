from django.urls import path
from hospitals.views import index
urlpatterns = [
    path('', index, name="index.html")
]
