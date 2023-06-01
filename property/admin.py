from django.contrib import admin

from property.models import Flat

class FlatAdmin(admin.ModelAdmin):
    list_display = ('town','address', 'price', 'owner', 'new_building', 'construction_year')
    list_editable =['new_building',]
    search_fields = ('town','address','owner',)
    readonly_fields = ["created_at"]
    list_filter = ['new_building', 'floor', 'rooms_number', 'has_balcony']

admin.site.register(Flat, FlatAdmin)
