from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('donors/logout',
         views.LogoutView.as_view(next_page='hospitals:index'), name="donor_logout"),
    path('', include("hospitals.urls", namespace="hospitals")),
    path('donors/', include("donors.urls", namespace="donors"),),
    path('donors/login/', views.LoginView.as_view(template_name="donors/login.html",
                                                  redirect_field_name='hospital:donor-detail pk=donor.pk'), name="donor_login"),

]
