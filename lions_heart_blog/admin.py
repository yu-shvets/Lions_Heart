from django.contrib import admin
from lions_heart_blog.models import Post, Comment, Image, CompanyInformation, \
    CompanyImage, Phone, Address, Email, Banners


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


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class EmailInline(admin.TabularInline):
    model = Email
    extra = 0


class BannerInline(admin.TabularInline):
    model = Banners
    extra = 0


@admin.register(CompanyInformation)
class CompanyAdmin(admin.ModelAdmin):
    inlines = (PhoneInline, AddressInline, EmailInline, CompanyImageInline, BannerInline)

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True



