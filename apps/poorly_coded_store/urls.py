from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^checkout$', views.checkout),
    url(r"^view_order/(?P<order_id>\d+)$", views.view_order),
]