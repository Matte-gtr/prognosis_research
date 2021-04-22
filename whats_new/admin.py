from django.contrib import admin
from .models import Latest_Research_Year, Research_Update,\
    Site_Page, Site_Log


class Research_UpdateAdmin(admin.ModelAdmin):
    list_display = (
        'year',
        'update',
    )


admin.site.register(Latest_Research_Year)
admin.site.register(Research_Update, Research_UpdateAdmin)
admin.site.register(Site_Page)
admin.site.register(Site_Log)
