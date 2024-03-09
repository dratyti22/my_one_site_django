from django.contrib import admin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin


from .models import User

# admin.site.register(User)


@admin.register(User)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_superuser']
    search_fields = ["username", "last_name", 'first_name']

    inlines = [CartTabAdmin, OrderTabulareAdmin,]
