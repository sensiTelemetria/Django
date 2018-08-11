from django import forms
from .models import relatorio

class relatorioForm(forms.ModelForm):
    class Meta:
        model = relatorio
        fields = '__all__'
