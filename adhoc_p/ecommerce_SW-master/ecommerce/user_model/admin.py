# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import register_model, add_student
from django.contrib import admin

# Register your models here.

class register(admin.ModelAdmin):
    list_display = ['username' ,'email', 'timestamp', 'updated']
    search_fields = ['username', 'email']
    date_hierarchy = 'timestamp'
    readonly_fields = ['timestamp', 'updated']

    class meta:
        model = register_model

admin.site.register(register_model, register)


class student(admin.ModelAdmin):
    list_display = ['first_name', 'contact_number', 'email', 'Addmission_type', 'college']
    readonly_fields = ['timestamp', 'updated']
    search_fields = ['first_name', 'last_name', 'Addmission_type']
    prepopulated_fields = {"slug": ("first_name",)}

    class meta:
        model = add_student

admin.site.register(add_student, student)

