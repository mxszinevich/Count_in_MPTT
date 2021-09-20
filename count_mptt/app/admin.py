from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Topic


class CountryAdmin(DjangoMpttAdmin):
    pass
admin.site.register(Topic, CountryAdmin)