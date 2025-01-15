from django.contrib import admin
from .models import Account , Email_history , Email_passwords
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email' , 'first_name' , 'last_name' , 'last_login' , 'date_joined' , 'is_active')
    list_display_links = ('email' , 'first_name','last_name')
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)

    list_filter = ()
    filter_horizontal = ()
    fieldsets =()
admin.site.register(Account , AccountAdmin)

class Email_history_admin(admin.ModelAdmin):
    readonly_fields = ('sent_date',)
admin.site.register(Email_history , Email_history_admin)


admin.site.register(Email_passwords)