import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from api.models import Products, Quotation
from front.forms import FormQuotation
from front.utils import json2obj


class HomeView(View):
    form_class = FormQuotation
    template_name = 'front/home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse(
                'front:quotation',
                kwargs={
                    'slug': form.cleaned_data.get('destiny'),
                    'begin_date': "{:%Y-%m-%d}".format(
                        form.cleaned_data.get('begin_date')),
                    'end_date': "{:%Y-%m-%d}".format(
                        form.cleaned_data.get('end_date')),
                }
            ))

        return render(request, self.template_name, {'form': form})


class QuotationView(View):
    form_class = FormQuotation
    template_name = 'front/quotation.html'

    def get(self, request, *args, **kwargs):
        begin_date = datetime.strptime(
            kwargs.get('begin_date'), '%Y-%m-%d')
        end_date = datetime.strptime(
            kwargs.get('end_date'), '%Y-%m-%d')
        form = self.form_class(initial={
            'destiny': kwargs.get('slug'),
            'begin_date': begin_date,
            'end_date': end_date,
        })
        quotations = Quotation()
        products = Products()
        quotations = quotations.calculate(
            destination=kwargs.get('slug'),
            begin_date=begin_date,
            end_date=end_date
        )
        for quotation in quotations:
            product = products.list(quotation.get('code'))
            hospital_care = [e for e in product.get(
                'benefits') if e['code'] == '50'][0].get('coverage')
            luggage_insurance = [e for e in product.get(
                'benefits') if e['code'] == '42'][0].get('coverage')
            quotation['hospital_care'] = hospital_care
            quotation['luggage_insurance'] = luggage_insurance

        quotations = json.dumps(quotations)
        quotations = json2obj(quotations)
        return render(
            request, self.template_name,
            {'form': form, 'quotations': quotations})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse(
                'front:quotation',
                kwargs={
                    'slug': form.cleaned_data.get('destiny'),
                    'begin_date': "{:%Y-%m-%d}".format(
                        form.cleaned_data.get('begin_date')),
                    'end_date': "{:%Y-%m-%d}".format(
                        form.cleaned_data.get('end_date')),
                }
            ))

        return render(request, self.template_name, {'form': form})


class CoverageView(View):
    template_name = 'front/coverage.html'

    def get(self, request, *args, **kwargs):
        begin_date = datetime.strptime(
            kwargs.get('begin_date'), '%Y-%m-%d')
        end_date = datetime.strptime(
            kwargs.get('end_date'), '%Y-%m-%d')
        destination = kwargs.get('slug')
        product_id = kwargs.get('product_id')

        quotations = Quotation()
        products = Products()

        quotations = quotations.calculate(
            destination=destination,
            begin_date=begin_date,
            end_date=end_date
        )
        quotation = [q for q in quotations if q['code'] == str(product_id)][0]
        quotation = json.dumps(quotation)
        quotation = json2obj(quotation)
        product = products.list(product_id)
        product = json.dumps(product)
        product = json2obj(product)

        return render(request, self.template_name, {
            'product': product,
            'quotation': quotation
        })


class PurchaseView(View):
    pass
