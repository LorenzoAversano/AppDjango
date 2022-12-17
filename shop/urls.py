from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('view_product/<int:id>/', views.view_product, name='view_product'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
]


