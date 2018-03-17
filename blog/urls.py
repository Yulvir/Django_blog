from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^(?P<username>[a-zA-Z0-9]+)/post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/post/new/$', views.post_new, name='post_new'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile, name='get_user_profile'),
    url(r'^like-blog/$', views.like_count_blog, name='like_count_blog'),
    url(r'^add-comment-to-post/$', views.add_comment_to_post, name='click_add_comment'),
]