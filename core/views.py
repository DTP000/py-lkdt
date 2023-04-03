from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, CreateView, FormView, View, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Category, Product

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