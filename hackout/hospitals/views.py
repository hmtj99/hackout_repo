from django.shortcuts import render, get_object_or_404
from hospitals.models import Hospital, Entry
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy


class HospitalListView(ListView):
    model = Hospital
    template_name = "hospitals/hospital_list.html"


class HospitalDetailView(DetailView):
    model = Hospital
    template_name = "hospitals/hospital_detail.html"


class HospitalCreateView(CreateView):
    model = Hospital
    fields = ['name', 'address', 'location']
    template_name = "hospitals/hospital_create.html"
    success_url = reverse_lazy('hospitals:thanks')


class EntryCreateView(CreateView):
    model = Entry
    fields = ['blood_group', 'hospital', 'quantity']
    template_name = "hospitals/entry_create.html"


class Thanks(TemplateView):
    template_name = "hospitals/thanks.html"


class EntrySuccessView(TemplateView):
    template_name = "hospitals/entry_created.html"


class EntryUpdateView(UpdateView):
    model = Entry
    template_name = "hospitals/entry_update.html"
    fields = ['quantity']


class EntryDeleteView(DeleteView):
    model = Entry
    template_name = "hospitals/entry_delete.html"

    def get_success_url(self):
        return reverse_lazy('hospitals:hospital-detail', kwargs={'pk': self.object.hospital.pk})
