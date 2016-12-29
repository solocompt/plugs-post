# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^Post/~create/$",
        view=views.PostCreateView.as_view(),
        name='Post_create',
    ),
    url(
        regex="^Post/(?P<pk>\d+)/~delete/$",
        view=views.PostDeleteView.as_view(),
        name='Post_delete',
    ),
    url(
        regex="^Post/(?P<pk>\d+)/$",
        view=views.PostDetailView.as_view(),
        name='Post_detail',
    ),
    url(
        regex="^Post/(?P<pk>\d+)/~update/$",
        view=views.PostUpdateView.as_view(),
        name='Post_update',
    ),
    url(
        regex="^Post/$",
        view=views.PostListView.as_view(),
        name='Post_list',
    ),
	url(
        regex="^PostSection/~create/$",
        view=views.PostSectionCreateView.as_view(),
        name='PostSection_create',
    ),
    url(
        regex="^PostSection/(?P<pk>\d+)/~delete/$",
        view=views.PostSectionDeleteView.as_view(),
        name='PostSection_delete',
    ),
    url(
        regex="^PostSection/(?P<pk>\d+)/$",
        view=views.PostSectionDetailView.as_view(),
        name='PostSection_detail',
    ),
    url(
        regex="^PostSection/(?P<pk>\d+)/~update/$",
        view=views.PostSectionUpdateView.as_view(),
        name='PostSection_update',
    ),
    url(
        regex="^PostSection/$",
        view=views.PostSectionListView.as_view(),
        name='PostSection_list',
    ),
	]
