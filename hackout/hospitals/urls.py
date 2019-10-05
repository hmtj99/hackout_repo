from django.urls import path
from hospitals.views import HospitalDetailView, HospitalCreateView, EntryCreateView, EntrySuccessView, EntryUpdateView, EntryDeleteView, SearchView, EntryListView, HospitalView

app_name = "hospitals"

urlpatterns = [
    path('', SearchView.as_view(), name="index"),
    path('hospitals-final', HospitalView, name="hospital-list-final"),
    path('<blood_group>', EntryListView.as_view(), name="search"),
    #   path('hospitals', HospitalListView.as_view(
    #      template_name="hospital_list.html"), name="hospital-list"),
    path('hospital/<int:pk>', HospitalDetailView.as_view(), name="hospital-detail"),
    path('hospital/new', HospitalCreateView.as_view(), name="hospital-create"),
    path('entry/new', EntryCreateView.as_view(), name="entry-create"),
    path("entry_success", EntrySuccessView.as_view(), name="entry-success"),
    path("entry/<int:pk>/update", EntryUpdateView.as_view(), name="entry-update"),
    path("entry/<int:pk>/delete", EntryDeleteView.as_view(), name="entry-delete")
]
