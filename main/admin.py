from django.contrib import admin
from . import models
from unfold.admin import ModelAdmin

@admin.register(models.State)
class StateAdmin(ModelAdmin):
    list_display = ['uuid', 'title', 'president']
    search_fields = ['title']
    list_filter = ['continent', 'president']



@admin.register(models.Region)
class RegionAdmin(ModelAdmin):
    list_display = ['uuid', 'title', 'governor']
    list_filter = ['state', 'governor']
    search_fields = ['title']



@admin.register(models.District)
class DistrictsAdmin(ModelAdmin):
    list_display = ['uuid', 'title']
    list_filter = ['region', 'governor']
    search_fields = ['title']



@admin.register(models.MFY)
class MFYAdmin(ModelAdmin):
    list_display = ['uuid', 'title', 'district']
    list_filter = ['chairman', 'district']
    search_fields = ['title']


@admin.register(models.Neighborhood)
class NeighborhoodAdmin(ModelAdmin):
    list_display = ['uuid', 'title']
    list_filter = ['MFY']
    search_fields = ['title']

@admin.register(models.House)
class HouseAdmin(ModelAdmin):
    list_display = ['uuid', 'house_number', 'a_b']
    list_filter = ['neighborhood', 'a_b']
    search_fields = ['house_number']



@admin.register(models.Human)
class HumanAdmin(ModelAdmin):
    list_display = ['uuid', 'name', 'house__house_number']
    list_filter = ['house', 'status', 'information']
    search_fields = ['name']

