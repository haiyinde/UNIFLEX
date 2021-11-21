from django.contrib import admin
from .models import Review, Comment
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display=['title', 'content','rank','user']

class CommentAdmin(admin.ModelAdmin):
    list_display=['content','user']

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)