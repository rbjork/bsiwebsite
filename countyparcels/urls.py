__author__ = 'dev'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(loaddata)$',views.upload_csv),
    url(r'^(specialselect)$',views.getSelectSpecial),
    url(r'^(mapview)$',views.showMapView),
    url(r'^(savetoshoppingcart)$',views.save2shoppingcart),
    url(r'^(requestpurchase)$', views.request4purchase),
    url(r'^(requestforquote)$',views.request4quote),
    url(r'^(buyform)$',views.buyform),
    url(r'^(quoteform)$',views.quoteform),
    url(r'^(sendquoterequest)$',views.sendrequest4quote)
]