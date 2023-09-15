from django.contrib import admin
from modelapp.models import *

@admin.register(Van)
class VanAdmin(admin.ModelAdmin):
    list_display=['id','vname','vcost']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display=['id','name','city','phone']
