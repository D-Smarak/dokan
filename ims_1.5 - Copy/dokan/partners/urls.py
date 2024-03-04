from django.urls import path
from . import views
from .views import (
    create_supplier,
    create_buyer,
    create_customer,
    create_delivery,
    update_supplier,
    update_buyer,
    update_customer,
    update_delivery,
    delete_supplier,
    delete_buyer,
    delete_customer,
    delete_delivery,
    supplier_list,
    buyer_list,
    customer_list,
    delivery_list,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('create-delivery/', create_delivery, name='create-delivery'),
    path('create-customer/', create_customer, name='create-customer'),
    
    path('update-supplier/<int:id>/', update_supplier, name='update-supplier'),
    path('update-buyer/<int:id>/', update_buyer, name='update-buyer'),
    path('update-customer/<int:id>/', update_customer, name='update-customer'),
    path('update-delivery/<int:id>/', update_delivery, name='update-delivery'),

    path('delete-supplier/<int:id>/', delete_supplier, name='delete-supplier'),
    path('delete-buyer/<int:id>/', delete_buyer, name='delete-buyer'),
    path('delete-customer/<int:id>/', delete_customer, name='delete-customer'),
    path('delete-delivery/<int:id>/', delete_delivery, name='delete-delivery'),

    path('supplier-list/', supplier_list, name='supplier-list'),
    path('buyer-list/', buyer_list, name='buyer-list'),
    path('customer-list/', customer_list, name='customer-list'),
    path('delivery-list/', delivery_list, name='delivery-list'),
]