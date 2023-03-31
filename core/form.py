from django import forms
from .models import Category

IS_DELETED_CHOICES = (
    (0, "Chưa xóa"),
    (1, "Đã xóa")
)

