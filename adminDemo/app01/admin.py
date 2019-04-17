from django.contrib import admin

# Register your models here.


from app01.models import Book, Publish, Author, AuthorDetail


class BookConfig(admin.ModelAdmin):
    #  list_display' must not be a ManyToManyField.
    list_display = ["title", "price", "publishDate", "publish"]
    list_display_links = ["price", "title"]

    list_filter = ["title", "publish", "authors"]
    search_fields = ["title", "price"]

    # 批量操作
    def patch_init(self, request, queryset):
        queryset.update(price=0)

    patch_init.short_description = "价格初始化"

    actions = [patch_init]


admin.site.register(Book, BookConfig)


class PublishConfig(admin.ModelAdmin):
    list_display = ["name", "email"]


admin.site.register(Publish, PublishConfig)

admin.site.register(Author)
admin.site.register(AuthorDetail)

print("_registry:-------->", admin.site._registry)
