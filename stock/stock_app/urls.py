from django.conf.urls import url

from . import views



""" url patterns """
urlpatterns = [
    url(r'^allocate/v1.0$', views.allocate_stock, name='allocate_stock'),
    url(r'^list/v1.0$', views.matched_unmatched_list, name='matched_unmatched_list'),
    url(r'^order/v1.0$', views.take_order, name='take_order'),

   ]
