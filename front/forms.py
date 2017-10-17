from django import forms
from api.models import Destinations


class FormQuotation(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FormQuotation, self).__init__(*args, **kwargs)
        destinations = Destinations()
        self.fields['destiny'].choices = (
            (d.get('slug'), d.get('name')) for d in destinations.list())

    destiny = forms.ChoiceField(label="Destino")
    begin_date = forms.DateField(
        label="Partida", widget=forms.widgets.DateInput(
            attrs={'class': 'date'}))
    end_date = forms.DateField(
        label="Retorno", widget=forms.widgets.DateInput(
            attrs={'class': 'date'}))
