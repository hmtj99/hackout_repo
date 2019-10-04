from django.urls import path
from hospitals.views import HospitalListView, HospitalDetailView

urlpatterns = [
    path('', HospitalListView.as_view(), name="hospital-list"),
    path('hospital/<int:pk>', HospitalDetailView.as_view(), name="hospital-detail")
]
