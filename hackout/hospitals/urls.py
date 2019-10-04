from django.urls import path
from hospitals.views import HospitalListView, HospitalDetailView, HospitalCreateView, Thanks, EntryCreateView, EntrySuccessView, EntryUpdateView, EntryDeleteView

app_name = "hospitals"

urlpatterns = [
    path('', HospitalListView.as_view(), name="hospital-list"),
    path('hospital/<int:pk>', HospitalDetailView.as_view(), name="hospital-detail"),
    path('hospital/new', HospitalCreateView.as_view(), name="hospital-create"),
    path('thanks', Thanks.as_view(), name="thanks"),
    path('entry/new', EntryCreateView.as_view(), name="entry-create"),
    path("entry_success", EntrySuccessView.as_view(), name="entry-success"),
    path("entry/<int:pk>/update", EntryUpdateView.as_view(), name="entry-update"),
    path("entry/<int:pk>/delete", EntryDeleteView.as_view(), name="entry-delete")
]
