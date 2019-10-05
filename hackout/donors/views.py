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
    model = Donor
    template_name = "donors/donor_list.html"


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
        location = form.cleaned_data['location']
        new_user = form.save()
        d = Donor(user=new_user, blood_group=blood_group,
                  location=location, phone=phone)
        d.save()
        return super().form_valid(form)
