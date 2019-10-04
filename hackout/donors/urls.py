from django.urls import path
from donors.views import DonorDetailView, DonorListView

app_name = 'donors'

urlpatterns = [
    path('', DonorListView.as_view(), name="donor-list"),
    path('<int:pk>', DonorDetailView.as_view(), name="donor-detail")
]
