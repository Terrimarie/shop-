from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    Product = (
        'name',
        'description',
        'price'
        'unit'
        'image',
    )