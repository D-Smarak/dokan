from django.urls import path
from . import views
from .views import (
    create_drop,
    update_drop,
    delete_drop,
    drop_list,
    create_product,
    update_product,
    delete_product,
    product_list,
    create_category,
    update_category,
    delete_category,
    category_list,
    create_stock,
    update_stock,
    delete_stock,
    stock_list,
)

urlpatterns = [
    path('create-drop/', create_drop, name='create-drop'),
    path('create-product/', create_product, name='create-product'),
    path('create-category/', create_category, name='create-category'),
    path('create-stock/', create_stock, name='create-stock'),
    
    path('update-drop/<int:id>/', update_drop, name='update-drop'),
    path('update-product/<int:id>/', update_product, name='update-product'),
    path('update-category/<int:id>/', update_category, name='update-category'),
    path('update-stock/<int:id>/', update_stock, name='update-stock'),

    path('delete-drop/<int:id>/', delete_drop, name='delete-drop'),
    path('delete-product/<int:id>/', delete_product, name='delete-product'),
    path('delete-category/<int:id>/', delete_category, name='delete-category'),
    path('delete-stock/<int:id>/', delete_stock, name='delete-stock'),

    path('drop-list/', drop_list, name='drop-list'),
    path('product-list/', product_list, name='product-list'),
    path('category-list/', category_list, name='category-list'),
    path('stock-list/', stock_list, name='stock-list'),
]