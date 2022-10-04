from django.contrib import admin

from main.models import Category, Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','price','category')
    list_editable = ('price',)
    list_filter = ('price','category')
    search_fields = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("title",)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Service,ServiceAdmin)