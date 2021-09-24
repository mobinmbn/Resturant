from django.contrib import admin
from .models import Food, Comment
# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name','add_time','rate')
    list_filter = ('category',)
    search_fields = ('name',)

admin.site.register(Food,FoodAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','add_time')
    list_filter = ('email',)
    search_fields = ('name',)

admin.site.register(Comment, CommentAdmin)
