from django import forms
from .models import alarme

class alarmeForm(forms.ModelForm):
    tags = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    usuarios = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    trigger = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = alarme
        fields = '__all__'
