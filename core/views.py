from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, CreateView, FormView, View
from django.urls import reverse_lazy
from .form import CategoryForm
from .models import Category, Product

# Create your views here.
# def index(request):
#     return render(request, 'pages/main.html')

class IndexHome(ListView):
    template_name = 'pages/demoContent.html'
    context_object_name = 'listView'

    def get_queryset(self):
        listObject = {
            'categoryList' : Category.objects.all(),
            'productList' : Product.objects.all()
        }
        return listObject

class CreateCategory(CreateView):
    model = Category
    fields = "__all__"
    template_name = 'pages/formCreate.html'
    success_url = reverse_lazy('index')