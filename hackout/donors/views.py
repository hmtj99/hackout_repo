from django.shortcuts import render
from django.views.generic import DetailView, ListView

from donors.models import Donor


class DonorDetailView(DetailView):
    model = Donor
    template_name = "donors/donor_detail.html"


class DonorListView(ListView):
    model = Donor
    template_name = "donors/donor_list.html"
