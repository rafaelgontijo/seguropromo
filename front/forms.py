from django import forms
from api.models import Destinations


class DateInput(forms.widgets.DateInput):
    input_type = 'date'


class FormQuotation(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FormQuotation, self).__init__(*args, **kwargs)
        destinations = Destinations()
        self.fields['destiny'].choices = (
            (d.get('slug'), d.get('name')) for d in destinations.list())

    destiny = forms.ChoiceField(label="Destino")
    begin_date = forms.DateField(
        label="Partida", widget=DateInput(attrs={'class': 'date'}))
    end_date = forms.DateField(
        label="Retorno", widget=DateInput(attrs={'class': 'date'}))
