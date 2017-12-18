from django.contrib import admin
from lions_heart_blog.models import Post, Comment, Image, CompanyInformation, CompanyImage


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Post)
class ItemAdmin(admin.ModelAdmin):
    inlines = (CommentInline, ImageInline)


class CompanyImageInline(admin.TabularInline):
    model = CompanyImage
    extra = 0


@admin.register(CompanyInformation)
class OrderAdmin(admin.ModelAdmin):
    inlines = (CompanyImageInline,)

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True



