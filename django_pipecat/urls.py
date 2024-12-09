# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'django_pipecat'
urlpatterns = [
    url(
        regex="^Pipelin/~create/$",
        view=views.PipelinCreateView.as_view(),
        name='Pipelin_create',
    ),
    url(
        regex="^Pipelin/(?P<pk>\d+)/~delete/$",
        view=views.PipelinDeleteView.as_view(),
        name='Pipelin_delete',
    ),
    url(
        regex="^Pipelin/(?P<pk>\d+)/$",
        view=views.PipelinDetailView.as_view(),
        name='Pipelin_detail',
    ),
    url(
        regex="^Pipelin/(?P<pk>\d+)/~update/$",
        view=views.PipelinUpdateView.as_view(),
        name='Pipelin_update',
    ),
    url(
        regex="^Pipelin/$",
        view=views.PipelinListView.as_view(),
        name='Pipelin_list',
    ),
	url(
        regex="^Stage/~create/$",
        view=views.StageCreateView.as_view(),
        name='Stage_create',
    ),
    url(
        regex="^Stage/(?P<pk>\d+)/~delete/$",
        view=views.StageDeleteView.as_view(),
        name='Stage_delete',
    ),
    url(
        regex="^Stage/(?P<pk>\d+)/$",
        view=views.StageDetailView.as_view(),
        name='Stage_detail',
    ),
    url(
        regex="^Stage/(?P<pk>\d+)/~update/$",
        view=views.StageUpdateView.as_view(),
        name='Stage_update',
    ),
    url(
        regex="^Stage/$",
        view=views.StageListView.as_view(),
        name='Stage_list',
    ),
	]
