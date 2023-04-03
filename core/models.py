from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
# Create your models here.

IS_DELETED_CHOICES = (
    (0, "Chưa xóa"),
    (1, "Đã xóa")
)

ROLE_CHOICES = (
    (1, 'Admin'),
    (2, 'Nhân viên'),
    (3, 'Khách hàng')
)

ORDER_STATUS_CHOICES = (
    (1, 'Chờ xác nhận'),
    (2, 'Đã xác nhận'),
    (3, 'Đã giao'),
    (4, 'Đã hủy đơn')
)

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Tên danh mục')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(choices=IS_DELETED_CHOICES, default=0, max_length=1)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    price = models.BigIntegerField(default=0)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    descr = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(choices=IS_DELETED_CHOICES, default=0)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Image(models.Model):    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.ImageField(null=False, blank=True, upload_to='photos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(choices=IS_DELETED_CHOICES, default=0)
    def admin_photo(self):
        return mark_safe('<img src="{}" width=100px;height=150px />'.format(self.image.url))
    admin_photo.short_description = 'image'
    admin_photo.allow_tags = True

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=254)
    total_price = models.BigIntegerField(default=0)
    note = models.TextField(blank=True, null=True)
    order_status = models.IntegerField(choices= ORDER_STATUS_CHOICES, default=1)
    product = models.ManyToManyField(Product, through='OrderDetail')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(choices=IS_DELETED_CHOICES, default=0)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.BigIntegerField(default=0)
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(choices=IS_DELETED_CHOICES, default=0)
