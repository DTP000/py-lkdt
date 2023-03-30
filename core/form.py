from django import forms

IS_DELETED_CHOICES = (
    (0, "Chưa xóa"),
    (1, "Đã xóa")
)

class CategoryForm(forms.Form):
    name = forms.CharField(label='Tên Danh Mục')