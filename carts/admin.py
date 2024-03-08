from django.contrib import admin

from .models import Cart

# admin.site.register(Cart)


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ['product', 'quantity', 'created_timestamp']
    search_fields = ['product', 'quantity', 'created_timestamp']
    readonly_fields = ('created_timestamp',)
    extra = 1


@admin.register(Cart)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product_display', 'quantity']
    search_fields = ['user', 'product', 'quantity', 'created_timestamp']
    list_filter = ['product__name', 'quantity', 'created_timestamp']

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return 'Анонимный пользователь'

    def product_display(self, obj):

        return str(obj.product.name)
