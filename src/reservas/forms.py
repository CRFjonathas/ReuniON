from django import forms
from .models import Reuniao

class ReuniaoForm(forms.ModelForm):
    class Meta:
        model = Reuniao

        fields = [
            'titulo', 'data_reuniao', 'hora_teste', 'hora_inicio',
            'local', 'link_reuniao', 'solicitante', 'equipamentos', 'observacoes', 'status'
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'data_reuniao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_teste': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'local': forms.TextInput(attrs={'class': 'form-control'}),
            'link_reuniao': forms.URLInput(attrs={'class': 'form-control'}),
            'solicitante': forms.TextInput(attrs={'class': 'form-control'}),
            'equipamentos': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }