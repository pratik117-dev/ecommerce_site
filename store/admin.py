from django.contrib import admin
from .models import Product,Variation

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'prize', 'stock','category','modified_date')
    prepopulated_fields = {'slug':('product_name',)}

class variationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')


admin.site.register(Product,ProductAdmin)
admin.site.register(Variation, variationAdmin)