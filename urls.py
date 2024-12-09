# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'django_pipecat'
urlpatterns = [
    url(
        regex="^Pipeline/~create/$",
        view=views.PipelineCreateView.as_view(),
        name='Pipeline_create',
    ),
    url(
        regex="^Pipeline/(?P<pk>\d+)/~delete/$",
        view=views.PipelineDeleteView.as_view(),
        name='Pipeline_delete',
    ),
    url(
        regex="^Pipeline/(?P<pk>\d+)/$",
        view=views.PipelineDetailView.as_view(),
        name='Pipeline_detail',
    ),
    url(
        regex="^Pipeline/(?P<pk>\d+)/~update/$",
        view=views.PipelineUpdateView.as_view(),
        name='Pipeline_update',
    ),
    url(
        regex="^Pipeline/$",
        view=views.PipelineListView.as_view(),
        name='Pipeline_list',
    ),
	url(
        regex="^Component/~create/$",
        view=views.ComponentCreateView.as_view(),
        name='Component_create',
    ),
    url(
        regex="^Component/(?P<pk>\d+)/~delete/$",
        view=views.ComponentDeleteView.as_view(),
        name='Component_delete',
    ),
    url(
        regex="^Component/(?P<pk>\d+)/$",
        view=views.ComponentDetailView.as_view(),
        name='Component_detail',
    ),
    url(
        regex="^Component/(?P<pk>\d+)/~update/$",
        view=views.ComponentUpdateView.as_view(),
        name='Component_update',
    ),
    url(
        regex="^Component/$",
        view=views.ComponentListView.as_view(),
        name='Component_list',
    ),
	]
