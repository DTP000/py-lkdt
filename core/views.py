from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest,HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, CreateView, FormView, View, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Category, Product, Order, OrderDetail, User
from core.form import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import json
from django.views.decorators.csrf import csrf_exempt

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
class DetailCard(ListView):
    model = Product
    template_name = 'pages/cart.html'
    context_object_name = 'listView'

def DetailProductApi(request, id):
    product = Product.objects.get(id = id)
    if not product:
        return JsonResponse(
            {
                "err_code": 232,
                "err_msg": "Khong tim thay san pham",
            }
        )
    return JsonResponse(
            {
                "err_code": 0,
                "err_msg": "Thành công",
                "data": {
                    "id": id,
                    "name": product.name,
                    "quantity": product.quantity,
                    "price": product.price,
                    "descr": product.descr,
                }
            }
        )
@csrf_exempt
def Checkout(request):
    if not request.user.is_authenticated:
        return JsonResponse(
            {
                "err_code": 532,
                "err_msg": "Chua dang nhap",
                "data": {
                    "id": 1,
                }
            }
        )

    data = json.loads(request.body)
    name = data['name']
    phone = data['phone']
    address = data['address']
    total_price = data['total_price']
    note = data['note']
    items = data['items']
    # user = User.objects.get(id=1)
    order = Order.objects.create(user=request.user, name=name, phone=phone, address=address, total_price=total_price, note=note)
    order.save()
    for item in items:
        product = Product.objects.get(id=item['product_id'])
        orderDetail = OrderDetail.objects.create(order=order, product=product, quantity=item['quantity'], price=item['price'])
        orderDetail.save()
    return JsonResponse(
            {
                "err_code": 0,
                "err_msg": "Thành công",
                "data": {
                    "id": order.id,
                },
                "user": request.user.id
            }
        )


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