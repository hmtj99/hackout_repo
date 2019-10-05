from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

BLOOD_GROUPS = (
    ("A+", "A+"),
    ("A-", "A-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("O+", "O+"),
    ("O-", "O-"),
)


class DonorForm(UserCreationForm):
    blood_group = forms.ChoiceField(choices=BLOOD_GROUPS)
    phone = forms.IntegerField()
    city = forms.CharField()
    longitude = forms.FloatField()
    latitude = forms.FloatField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'phone', 'blood_group', ]
