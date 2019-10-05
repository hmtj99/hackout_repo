from django import forms
from hospitals.models import Hospital

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


class SearchForm(forms.Form):
    blood_group_input = forms.ChoiceField(choices=BLOOD_GROUPS)
