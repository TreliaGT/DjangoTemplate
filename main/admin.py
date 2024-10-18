from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Fields to display in the list view
    search_fields = ('name', 'email')  # Fields to search by in the admin interface
    ordering = ('-created_at',)  # Order by creation date, newest first
