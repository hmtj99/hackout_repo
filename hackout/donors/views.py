from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, FormView, TemplateView
from django.contrib.auth.models import User
from donors.models import Donor
from donors.forms import DonorForm
from django.contrib.auth.mixins import LoginRequiredMixin


class DonorDetailView(DetailView, LoginRequiredMixin):
    model = Donor
    template_name = "donors/donor_detail.html"


class DonorListView(ListView):
    template_name = "donors/donor_list.html"

    def get_queryset(self):
        return Donor.objects.filter(blood_group=self.kwargs['blood_group'])


class DonorRegThanksView(TemplateView):
    template_name = "donors/donor_create_success.html"


class DonorCreateView(FormView):
    model = User
    form_class = DonorForm
    success_url = 'thanks'
    template_name = 'donors/donor_create.html'

    def form_valid(self, form):
        phone = form.cleaned_data['phone']
        blood_group = form.cleaned_data['blood_group']
        city = form.cleaned_data['city']
        longitude = form.cleaned_data['longitude']
        latitude = form.cleaned_data['latitude']
        new_user = form.save()
        d = Donor(user=new_user, blood_group=blood_group,
                  city=city, phone=phone, longitude=longitude, latitude=latitude)
        d.save()
        return super().form_valid(form)
