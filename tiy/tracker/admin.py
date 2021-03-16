from django.contrib import admin

from .models import Asset, Broker, Exchange, Trade

# Register your models here.
class AssetAdmin(admin.ModelAdmin):
    ordering = ['symbol']
    list_filter = ['type']


admin.site.register(Asset, AssetAdmin)
admin.site.register(Broker)
admin.site.register(Exchange)
admin.site.register(Trade)
