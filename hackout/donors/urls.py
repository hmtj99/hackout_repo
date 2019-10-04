from django.urls import path
from donors.views import DonorDetailView, DonorListView, DonorCreateView, DonorRegThanksView

app_name = 'donors'

urlpatterns = [
    path('', DonorListView.as_view(), name="donor-list"),
    path('<int:pk>', DonorDetailView.as_view(), name="donor-detail"),
    path('new', DonorCreateView.as_view(), name="donor-create"),
    path('thanks', DonorRegThanksView.as_view(), name="thanks"),
]
