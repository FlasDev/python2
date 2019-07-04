from django.contrib import admin

# Register your models here.
from django.contrib import admin
from computers.models import Computer, OS, Producer

# admin.site.register(Computer)
# admin.site.register(OS)
# admin.site.register(Computer, OS)

admin.site.site_header = "Custom Admin"
admin.site.site_title = "Computer Admin"
admin.site.index_title = "Welcome to Computer Administration"


class OSInline(admin.StackedInline):
    model = OS


class ProducerInline(admin.StackedInline):
    model = Producer


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    inlines = [
        OSInline,
        ProducerInline
    ]
