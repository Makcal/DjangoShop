from django.urls import path, re_path

from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<int:product_id>/', views.product, name='product'),
    path('search/<str:query>/', views.search, name='search'),
    path('search_redirect/', views.search_redirect, name='search_redirect'),
    path('new/', views.new_product, name='new_product'),
    path('add/', views.add_product, name='add_product'),
    re_path(r'^.*$', views.to_home),
]
