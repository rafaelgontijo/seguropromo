from django.conf.urls import url
from django.views.generic.base import TemplateView
from front.views import CoverageView, HomeView, QuotationView, PurchaseView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^sucesso', TemplateView.as_view(template_name='front/sucess.html'), name='success'),
    url(r'^pesquisa/(?P<slug>[\w-]+)/(?P<begin_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})$',
        QuotationView.as_view(), name='quotation'),
    url(r'^cobertura/(?P<product_id>\d+)/(?P<slug>[\w-]+)/(?P<begin_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})$',
        CoverageView.as_view(), name='coverage'),
    url(r'^pedido/(?P<product_id>\d+)/(?P<slug>[\w-]+)/(?P<begin_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})$',
        PurchaseView.as_view(), name='order'),
]
