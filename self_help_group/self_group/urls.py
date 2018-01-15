from django.conf.urls import url
from . import views

app_name = 'self_group'
urlpatterns = [
    url(r'^$', views.MembersList.as_view(), name='members'),
    url(r'^create_member/$', views.MemberCreate.as_view(), name='create_member'),
    url(r'^group_day/$', views.day, name='day'),
    url(r'^unga/$', views.UngaCreate.as_view(), name='unga'),
]