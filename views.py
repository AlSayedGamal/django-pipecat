# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Pipeline,
	Component,
)


class PipelineCreateView(CreateView):

    model = Pipeline


class PipelineDeleteView(DeleteView):

    model = Pipeline


class PipelineDetailView(DetailView):

    model = Pipeline


class PipelineUpdateView(UpdateView):

    model = Pipeline


class PipelineListView(ListView):

    model = Pipeline


class ComponentCreateView(CreateView):

    model = Component


class ComponentDeleteView(DeleteView):

    model = Component


class ComponentDetailView(DetailView):

    model = Component


class ComponentUpdateView(UpdateView):

    model = Component


class ComponentListView(ListView):

    model = Component

