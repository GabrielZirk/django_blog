from django.contrib import admin
from blog.models import Post, Author, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "date")
    ordering = ('date',)
    
    class Meta:
        verbose_name_plural = "Post"


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "mail")
    ordering=('last_name', 'first_name')
    
    class Meta:
        verbose_name_plural = "Author"
        

class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)
    
    class Meta:
        verbose_name_plural = "Tag"


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
