# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CustomerAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'username',
        'phone',
        'email',
        'password',
        'date_add',
        'date_up',
        'image',
    )
    list_filter = (
        'date_add',
        'date_up',
        'id',
        'name',
        'username',
        'phone',
        'email',
        'password',
        'date_add',
        'date_up',
        'image',
    )
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Customer, CustomerAdmin)
