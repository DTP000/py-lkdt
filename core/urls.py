from django.urls import path
from . import views

app_name = 'category'
urlpatterns = [
    # path('', views.index)
    path('', views.IndexHome.as_view(), name='index'),
    path('category/create', views.CreateCategory.as_view(), name='create'),
    path('category/detail/<int:pk>', views.DetailCategory.as_view(), name='detail'),
    path('category/update/<int:pk>', views.UpdateCategory.as_view(), name='update'),
]