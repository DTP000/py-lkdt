from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

IS_DELETED_CHOICES = (
    (0, "Chưa xóa"),
    (1, "Đã xóa")
)

class RegisterForm(forms.Form): 
    username = forms.CharField(label='Username', max_length=50)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    passwordclaim = forms.CharField(label='Xác nhận mật khẩu', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            passwordclaim = self.cleaned_data['passwordclaim']
            if password==passwordclaim and password:
                return passwordclaim
        raise forms.ValidationError("Nhập mật khẩu không hợp lệ")
    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'^\W+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")
    def clean_email(self):
        email = self.cleaned_data['email']
        if re.search(r' ', email):
            raise forms.ValidationError("Email có khoẳng trống")
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError("Email đã tồn tại")
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'])
