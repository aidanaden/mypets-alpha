from django.contrib import admin
from store.models import Merchant, Category, AnimalCategory, Product

admin.site.register(Merchant)
admin.site.register(Category)
admin.site.register(AnimalCategory)
admin.site.register(Product)