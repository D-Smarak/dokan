from django.urls import path
from views import (
    create_order,
    update_order,
    delete_order,
    order_list,
)

urlpatterns = [
    path('create-order/', create_order, name='create-order'),
    path('update-order/<int:id>/', update_order, name='update-order'),
    path('delete-order/<int:id>/', delete_order, name='delete-order'),
    path('order-list/', order_list, name='order-list'),
]