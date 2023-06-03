from django.contrib import admin

from property.models import Flat, Complaint, Owner


class FlatsInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner', 'flat']


class FlatAdmin(admin.ModelAdmin):
    list_display = ['town','address', 'price',# 'owner',
                    'new_building', 'construction_year']
    list_editable =['new_building',]
    search_fields = ['town','address',#'owner',
                    ]
    readonly_fields = ["created_at"]
    list_filter = ['new_building', 'rooms_number',
                   'has_balcony', 'floor']
    raw_id_fields = ['likes']
    inlines = [FlatsInline]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat']

    
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['owner',]
    raw_id_fields = ['flats']
    inlines = [FlatsInline]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
