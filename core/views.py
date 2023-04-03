from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest,HttpResponseRedirect
from django.views.generic import ListView, CreateView, FormView, View, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Category, Product
from core.form import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
# def index(request):
#     return render(request, 'pages/main.html')

class IndexHome(ListView):
    template_name = 'pages/main.html'
    context_object_name = 'listView'

    def get_queryset(self):
        listObject = {
            'categoryList' : Category.objects.all(),
            'productList' : Product.objects.all()
        }
        return listObject

class CreateCategory(CreateView):
    model = Category
    fields = ['name']
    template_name = 'pages/formCreate.html'
    success_url = reverse_lazy('category:index')

class DetailCategory(DetailView):
    model = Product
    template_name = 'pages/product__detail.html'

class UpdateCategory(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'pages/formCreate.html'
    success_url = reverse_lazy('category:index')

def Register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../accounts/login')
    return render (request, 'registration/register.html',{'form': form})
def Login(request):
    if request.method == 'POST':
        if  request.user.is_authenticated:
            messages.warning(request, "Bạn đã đăng nhập")
            return redirect('')
        else:
            if request.method == 'POST':
                name = request.POST.get('username') 
                password = request.POST.get('password') 
                user = authenticate(request, username=name, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Đăng nhập thành công")
                    return redirect('category:index')
                else:
                    messages.error(request, "Tài khoản hoặc mật khẩu không chính xác!!!")
                    return redirect('category:login')     
    return render(request, "registration/login.html") 

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Đăng xuất thành công")
    return redirect("category:index")