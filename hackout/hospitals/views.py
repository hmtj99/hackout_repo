from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from hospitals.models import Hospital, Entry
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from hospitals.forms import SearchForm
from django.contrib.auth.mixins import LoginRequiredMixin


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


class HospitalDetailView(DetailView):
    login_url = 'donor_login'
    model = Hospital
    template_name = "hospitals/hospital_detail.html"


class HospitalCreateView(CreateView):
    model = Hospital
    fields = ['name', 'address', 'location']
    template_name = "hospitals/hospital_create.html"

    def form_valid(self, form):
        this_name = form.cleaned_data['name']
        this_address = form.cleaned_data['address']
        this_location = form.cleaned_data['location']
        current_user = self.request.user
        h = Hospital(user=current_user, name=this_name,
                     address=this_address, location=this_location)
        h.save()
        return HttpResponseRedirect(reverse("hospitals:hospital-list-final"))


class EntryCreateView(LoginRequiredMixin, CreateView):
    login_url = 'donor_login'
    model = Entry
    fields = ['blood_group', 'hospital', 'quantity']
    template_name = "hospitals/entry_create.html"


class EntrySuccessView(TemplateView):
    template_name = "hospitals/entry_created.html"


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'donor_login'
    model = Entry
    template_name = "hospitals/entry_update.html"
    fields = ['quantity']


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'donor_login'
    model = Entry
    template_name = "hospitals/entry_delete.html"

    def get_success_url(self):
        return reverse_lazy('hospitals:hospital-detail', kwargs={'pk': self.object.hospital.pk})


def HospitalView(request):
    current_user = request.user
    hospitals = Hospital.objects.filter(user=current_user)
    return render(request, "hospitals/new.html", context={"hospitals": hospitals})
