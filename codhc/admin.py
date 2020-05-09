from django.contrib import admin

# Register your models here.
from .models import Post, Comment
#from PARENT.account.models import Account

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin (admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['user', 'title']}),
        ('Post Text', {'fields': ['post_text']}),
    ]

class CommentAdmin (admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['user', 'post']}),
        ('Comment Text', {'fields': ['comment_text']}),
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)