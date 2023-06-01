from django.contrib import admin

from property.models import Flat, Complaint

class FlatAdmin(admin.ModelAdmin):
    list_display = ('town','address', 'price', 'owner', 'new_building', 'construction_year')
    list_editable =['new_building',]
    search_fields = ('town','address','owner',)
    readonly_fields = ["created_at"]
    list_filter = ['new_building', 'floor', 'rooms_number', 'has_balcony']

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat']

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
