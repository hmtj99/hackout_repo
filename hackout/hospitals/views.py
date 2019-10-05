from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from hospitals.models import Hospital, Entry
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from hospitals.forms import SearchForm


class SearchView(FormView):
    form_class = SearchForm
    template_name = "hospitals/index.html"

    def form_valid(self, form):
        self.form = form
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        bg = self.form.cleaned_data['blood_group_input']
        return reverse('hospitals:search', kwargs={'blood_group': bg})


class EntryListView(ListView):
    template_name = "hospitals/entry_list.html"

    def get_queryset(self):
        return Entry.objects.filter(blood_group=self.kwargs['blood_group'])


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
