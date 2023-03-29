from django.contrib import admin
from .models import Category, Image, Product, Order, OrderDetail, User

# Register your models here.
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)
# admin.site.register(User)
