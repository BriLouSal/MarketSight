from django.contrib import admin

# Register your models here.



from .models import User




class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')
    search_fields = ('name', 'symbol')
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page = 10


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    list_filter = ('username',)



