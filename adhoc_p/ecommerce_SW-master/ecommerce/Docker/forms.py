from django import forms

DISPLAY_CHOICES = (
    ("docker", "Docker"),
    ("spark", "spark")
)

class MyForm(forms.Form):
    display_type = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES)