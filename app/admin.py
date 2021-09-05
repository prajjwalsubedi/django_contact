from django.contrib import admin
#from django.contrib.auth.models import Group
from . import models


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'gender', 'email', 'info', 'phone', 'date_added')
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('name', 'gender', 'email', 'info', 'phone')
    list_filter = ('gender', 'date_added')

admin.site.register(models.Contact, ContactAdmin)

#admin.site.unregister(Group)



