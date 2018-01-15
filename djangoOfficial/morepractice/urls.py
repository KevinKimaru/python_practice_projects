from django.conf.urls import url
from django.contrib.auth import views as auth_views

from morepractice.views import MyFormView, BookList, BookDetail, BookListFiltered, BookListArgs, AuthorDetailView, \
    BookClassView, StudentDelete, StudentUpdate, StudentCreate
from . import views

app_name = 'morepractice'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index_book/$', views.index_book, name='index_book'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^oops/$', views.oops, name='oops'),
    url(r'^index_many/$', views.index_many, name='index_many'),
    url(r'^(?P<writer_id>[0-9]+)/publish/$', views.publish, name='publish'),
    # url(r'^auth/$', views.authm),

    url(r'^formview/$', MyFormView.as_view(), name='my_form_view'),

    url(r'login/$', views.login_user, name='login'),
    # url(r'login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', views.logout_user, name='logout'),
    # url(r'^logout/$', auth_views.LogoutView.as_view()),
    # url(r'^change_password/$', auth_views.PasswordChangeView.as_view()),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^change_admin_password/$', views.change_admin_password, name='change_admin_password'),
    url(r'^official_login/$', views.official_login, name='official_login'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^create_user/$', views.create_user, name='create_user'),


    url(r'^booklist/$', BookList.as_view()),
    url(r'^booklistfiltered/$', BookListFiltered.as_view()),
    url(r'^booklistArgs/([\w-]+)/$', BookListArgs.as_view()),
    url(r'^(?P<pk>[0-9]+)/bookdetail/$', BookDetail.as_view()),
    url(r'^authors/(?P<pk>[0-9]+)/$', AuthorDetailView.as_view()),

    url(r'^bookclass/$', BookClassView.as_view()),

    url(r'student/add/$', StudentCreate.as_view(), name='author-add'),
    url(r'student/(?P<pk>[0-9]+)/$', StudentUpdate.as_view(), name='author-update'),
    url(r'student/(?P<pk>[0-9]+)/delete/$', StudentDelete.as_view(), name='author-delete'),

]
