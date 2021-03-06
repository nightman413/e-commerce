from django.contrib import admin
from product.models import Category, Product , Images

# Register your models here.

class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category' , 'price', 'amount', 'image_tag' , 'status']
    readonly_fields = ['image_tag']
    list_filter = ['status','category']
    inlines = [ProductImagesInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image_tag']
    readonly_fields = ['image_tag']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)