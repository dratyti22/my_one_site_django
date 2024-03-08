from django.contrib import admin


from .models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discout']
    list_editable = ["quantity", "discout"]
    search_fields = ["name", "description"]
    list_filter = ['quantity', 'price', 'discout', 'category']

    fields = [
        'name',
        'category',
        'slug',
        'description',
        ('price',
         'discout'),
        'quantity',
        'image'
    ]
