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
        (None,               {'fields': ['pub_date', 'score']}),
        ('Post Text', {'fields': ['post_text']}),
    ]
    inlines = [CommentInline]
    list_display = ('title', 'pub_date',)
    list_filter = ['pub_date']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)