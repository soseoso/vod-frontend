from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^new/$', views.post_new, name='post_new'),
    url('^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url('^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url('^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),

    url('^(?P<post_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
    url('^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    url('^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),

]
