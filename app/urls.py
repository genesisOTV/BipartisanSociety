from django.conf.urls import url
from . import views

#url(r'^$', views.index, name='index'),

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('home_a', views.TESTER_homea.as_view(), name='demoIndexA'),
]
