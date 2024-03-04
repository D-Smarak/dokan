from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import IntegrityError
from django.forms import ModelForm
from users.models import CustomUser
from .models import Order
from .forms import OrderForm


# Order views
@login_required(login_url='login')
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Retrieve the workspace identifier of the current user
            workspace_identifier = request.user.id
            
            # Create the Supplier object
            order = form.save(commit=False)
            order.workspace_identifier = workspace_identifier
            order.save()
            return redirect('supplier-list')
    else:
        form = OrderForm()

    context = {'form': form}
    return render(request, 'sales/create_supplier.html', context)


@login_required(login_url='login')
def order_list(request):
    workspace_identifier = request.user.id
    order = Order.objects.filter(workspace_identifier=workspace_identifier)
    return render(request, 'sales/order_list.html', {'order': order})



@login_required(login_url='login')
def update_order(request, id):
    order = None
    forms = OrderForm()
    workspace_identifier = request.user.id
    if request.method == 'POST':
        try:
            order = Order.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
            forms = OrderForm(request.POST)
            if forms.is_valid():
                try:
                    order.product = forms.cleaned_data['product']
                    order.buyer = forms.cleaned_data['buyer']
                    order.customer = forms.cleaned_data['customer']
                    order.description = forms.cleaned_data['description']
                    order.quantity = forms.cleaned_data['quantity']
                    order.sales_date = forms.cleaned_data['sales_date']
                    order.payment_method = forms.cleaned_data['payment_method']
                    order.total_amount = forms.cleaned_data['total_amount']
                    order.tax_amount = forms.cleaned_data['tax_amount']
                    order.discount_amount = forms.cleaned_data['discount_amount']
                    order.sub_total = forms.cleaned_data['sub_total']
                    order.payment_status = forms.cleaned_data['payment_status']
                    order.transaction_id = forms.cleaned_data['transaction_id']
                    order.tracking_number = forms.cleaned_data['tracking_number']
                    order.notes = forms.cleaned_data['notes']
                    order.quantity = forms.cleaned_data['quantity']
                    order.supplier = forms.cleaned_data['supplier']
                    order.location = forms.cleaned_data['location']
                    order.status = forms.cleaned_data['status']
                    order.category = forms.cleaned_data['category']
                    order.delivery = forms.cleaned_data['delivery']

                    order.save()
                    return redirect('order-list')
                except IntegrityError as e:
                    forms.add_error(None, 'Input Value must be unique')
        except Order.DoesNotExist:
            return HttpResponse("Order does not exist", status=404)

    if order is None:
        try:
            order = Order.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
        except Order.DoesNotExist:
            return HttpResponse("Order does not exist", status=404)

    return render(request, 'sales/update_order.html', {'order': order, 'form': forms})


@login_required(login_url='login')
def delete_order(request, id):
    workspace_identifier = request.user.id
    order = Order.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
    order.delete()
    return redirect('order-list')