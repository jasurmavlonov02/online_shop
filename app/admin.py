from django.contrib import admin
from django.contrib.auth.models import Group, User

from app.models import Product, Comment, Category, Order

# Register your models here.

admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'image', 'is_expensive')
    list_filter = ('category',)

    def is_expensive(self, obj):
        return obj.price > 10_000

    is_expensive.boolean = True


admin.site.unregister(User)
admin.site.unregister(Group)
