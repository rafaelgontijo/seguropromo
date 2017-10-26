from django.conf.urls import url
from purchase.views import DetailPurchase, ListPurchase

urlpatterns = [
    url(r'^$', ListPurchase.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', DetailPurchase.as_view(), name='detail'),
]
