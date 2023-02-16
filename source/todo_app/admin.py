from django.contrib import admin

from todo_app.models import TODO


# Register your models here.

class TODOAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'date_of_completion')
    list_filter = ('title', 'status', 'date_of_completion')
    search_fields = ('id', 'title', 'description', 'status', 'date_of_completion')
    list_editable = ('title', 'description', 'status', 'date_of_completion')


admin.site.register(TODO, TODOAdmin)
