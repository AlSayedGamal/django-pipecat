# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (
   Pipelin,
   Stage,
)


@admin.register(Pipelin)
class PipelinAdmin(admin.ModelAdmin):
    pass


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    pass



