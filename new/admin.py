from django.contrib import admin
from .models import Models,Cars

admin.site.register(Models)

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk','car_name','car_color','created_at','updated_at','model')
    list_display_links = ('car_name','pk')
    list_editable = ('model','car_color')
    list_filter = ('model','car_color')
    search_fields = ('pk','car_name','car_bio')
    list_per_page = 3

admin.site.register(Cars,PostAdmin)