from django.contrib import admin
from lions_heart_cart.models import Order, OrderItem


class OrderItemInline(admin.StackedInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline,
    ]

admin.site.register(Order, OrderAdmin)
