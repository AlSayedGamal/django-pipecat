# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Pipelin,
	Stage,
)


class PipelinCreateView(CreateView):

    model = Pipelin


class PipelinDeleteView(DeleteView):

    model = Pipelin


class PipelinDetailView(DetailView):

    model = Pipelin


class PipelinUpdateView(UpdateView):

    model = Pipelin


class PipelinListView(ListView):

    model = Pipelin


class StageCreateView(CreateView):

    model = Stage


class StageDeleteView(DeleteView):

    model = Stage


class StageDetailView(DetailView):

    model = Stage


class StageUpdateView(UpdateView):

    model = Stage


class StageListView(ListView):

    model = Stage

