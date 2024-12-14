from django.contrib import admin

from .models import Category, Post

admin.site.empty_value_display = "Не задано"


class PostInline(admin.TabularInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (PostInline,)
    list_display = (
        "title",
        "description",
        "slug",
        "is_published",
    )
    list_editable = ("is_published",)
    search_fields = ("title",)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "text",
        "pub_date",
        "author",
        "category",
        "is_published",
        "created_at",
    )
    list_editable = ("is_published", "category", "pub_date", "author")
    search_fields = ("title",)
    list_filter = ("is_published",)
    list_display_links = ("title",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
