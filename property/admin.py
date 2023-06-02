from django.contrib import admin

from property.models import Flat, Complaint, Owner

class FlatAdmin(admin.ModelAdmin):
    list_display = ('town','address', 'price', 'owner', 'new_building', 'construction_year')
    list_editable =['new_building',]
    search_fields = ('town','address','owner',)
    readonly_fields = ["created_at"]
    list_filter = ['new_building', 'floor', 'rooms_number', 'has_balcony']
    raw_id_fields = ['likes']

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat']

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    
admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
