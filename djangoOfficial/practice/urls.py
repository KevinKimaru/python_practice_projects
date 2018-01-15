from django.conf.urls import url
from . import views

app_name = 'practice'

urlpatterns = [
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^name/$', views.get_name, name='name'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^article/$', views.article, name='article'),
    url(r'^index/$', views.index, name='index'),
]
