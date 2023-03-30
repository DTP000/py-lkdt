from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index)
    path('', views.IndexHome.as_view(), name='index'),
    path('category/create', views.CreateCategory.as_view(), name='create')
]