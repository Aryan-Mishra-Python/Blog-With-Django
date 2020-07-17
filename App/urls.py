from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^home/$', PostListView.as_view(), name="post_list"),
    url(r'^post/(?P<pk>\d+)$', PostDetailView.as_view(), name="post_detail"),
    url(r'^post/new$', CreatePostView.as_view(), name="post_new"),
    url(r'^post/(?P<pk>\d+)/edit/$', UpdatePostView.as_view(), name="post_edit"),
    url(r'^about/$', AboutView.as_view(), name="about"),

    url(r'^post/(?P<pk>\d+)/remove/$',
        PostDeleteView.as_view(), name="post_delete"),

    url(r'^drafts/$', DraftListView.as_view(), name='post_draft'),

    url(r'^post/(?P<pk>\d+)/comment/$',
        add_comment_to_post, name='add_comment_to_post'),

    url(r'^post/(?P<pk>\d+)/publish/$', publish_post, name='publish_post')
]
