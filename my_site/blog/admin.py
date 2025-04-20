from django.contrib import admin

from .models import Author,Tag,Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug":("title",)}
    list_display = ("title","slug","date",)
    search_fields = ("title","content",)
    ordering = ("-date",)


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)

