from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#import all models to show on dashboard
from partners.models import *
# from partners.models import supplier, buyer, customer, delivery
from warehouse.models import *
# from warehouse import import drop, product, category, stock
from sales.models import Order
from users.models import CustomUser
from extras.models import Season


@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_buyer = Buyer.objects.count()
    total_sales = Order.objects.count()
    total_customer = Customer.objects.count()
    stock = Stock.objects.all().order_by('-id')
    sales = Order.objects.all().order_by('-id')
    drop = Drop.objects.all().order_by('-id')
    context = {
        'product': total_product,
        'supplier': total_supplier,
        'buyer': total_buyer,
        'sales': total_sales,
        'customer': total_customer,
        'stock': stock,
        'sales': sales,
        'warehouse': drop,
    }
    return render(request, 'dashboard.html', context)
