from django.db import models

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
<<<<<<< HEAD
    name = models.CharField(max_length=100, )
=======
    name = models.CharField(max_length=100, verbose_name='Tên danh mục')
>>>>>>> 867f9a9701d4a765cd5ae007ac3cc7d6655e311b
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(choices=IS_DELETED_CHOICES, default=0, max_length=1)

    def __str__(self):
        return self.name

class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    role = models.IntegerField(max_length=1, choices=ROLE_CHOICES, default=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(choices=IS_DELETED_CHOICES, default=0, max_length=1)

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
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(choices=IS_DELETED_CHOICES, default=0)

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
