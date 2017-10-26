from django import forms
from api.models import Destinations
from localflavor.br.forms import BRCPFField, BRPhoneNumberField


class CommonForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CommonForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] = 'form-control ' + \
                    field.widget.attrs['class']
            else:
                field.widget.attrs['class'] = 'form-control'


class FormQuotation(CommonForm):
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


class FormPurchase(CommonForm):
    insured_cpf = BRCPFField(label="CPF")
    insured_name = forms.CharField(max_length=100, label="Nome")
    birth_date = forms.DateField(
        label="Data de Nascimento", widget=forms.widgets.DateInput(
            attrs={'class': 'date'}))
    card_name = forms.CharField(max_length=100, label="Nome no cartão")
    card_cpf = BRCPFField(label="CPF")
    card_number = forms.CharField(max_length=16, label="Número do cartão")
    card_mouth = forms.ChoiceField(choices=(
        ('', '--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ), label="Validade mês")
    card_year = forms.ChoiceField(choices=(
        ('', '----'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
        ('2031', '2031'),

    ), label="Validade ano")
    card_cvv = forms.CharField(max_length=4, label="CVV")
    buy_name = forms.CharField(max_length=100, label="Nome para contato")
    buy_email = forms.EmailField(label="Email para contato")
    buy_phone = BRPhoneNumberField(label="Telefone para contato")
