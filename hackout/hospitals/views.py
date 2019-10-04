from django.shortcuts import render
from hospitals.models import Hospital, Entry
from django.views.generic import ListView, DetailView


class HospitalListView(ListView):
    model = Hospital
    template_name = "hospitals/hospital_list.html"


class HospitalDetailView(DetailView):
    model = Hospital
    template_name = "hospitals/hospital_detail.html"
