from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from purchase.models import Purchase


class ListPurchase(ListView):
    model = Purchase


class DetailPurchase(DetailView):
    model = Purchase
