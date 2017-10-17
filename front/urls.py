from django.conf.urls import url
from front.views import HomeView, QuotationView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^pesquisa/(?P<slug>[\w-]+)/(?P<begin_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})$',
        QuotationView.as_view(), name='quotation'),
]
