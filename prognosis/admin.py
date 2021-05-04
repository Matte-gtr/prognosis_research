from django.contrib import admin
from .models import Quote_of_note


class Quote_of_note_admin(admin.ModelAdmin):
    list_display = (
        'date_added',
        'quote',
    )


admin.site.register(Quote_of_note, Quote_of_note_admin)
