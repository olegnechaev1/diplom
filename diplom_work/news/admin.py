from django.contrib import admin
from .models import News, Comment, Like


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'link',
        'published',
        'created_at',
        'source',
    )
    
    search_fields = ['source']
    
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'comment',
        'date',
    )    
    
    search_fields = ['author__username']

class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'comment_like',
    )
    
    search_fields = ['comment_like__author__username']
    
admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
