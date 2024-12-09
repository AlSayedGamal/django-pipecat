# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (
   Pipeline,
   Component,
)


@admin.register(Pipeline)
class PipelineAdmin(admin.ModelAdmin):
    pass


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    pass



