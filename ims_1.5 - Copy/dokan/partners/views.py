
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import IntegrityError
from django.forms import ModelForm

from users.models import CustomUser

from .models import (
    Supplier,
    Buyer,
    Customer,
    Delivery
)

from .forms import (
    SupplierForm,
    BuyerForm,
    CustomerForm,
    DeliveryForm
)



# Supplier views
@login_required(login_url='login')
def create_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            # Retrieve the workspace identifier of the current user
            workspace_identifier = request.user.id
            
            # Create the Supplier object
            supplier = form.save(commit=False)
            supplier.workspace_identifier = workspace_identifier
            supplier.save()
            return redirect('supplier-list')
    else:
        form = SupplierForm()

    context = {'form': form}
    return render(request, 'partners/create_supplier.html', context)


@login_required(login_url='login')
def supplier_list(request):
    # Retrieve the workspace identifier of the current user
    workspace_identifier = request.user.id
    # Filter Season objects based on the workspace identifier
    supplier = Supplier.objects.filter(workspace_identifier=workspace_identifier)
    return render(request, 'partners/supplier_list.html', {'supplier': supplier})


@login_required(login_url='login')
def update_supplier(request, id):
    supplier = None
    forms = SupplierForm()
    workspace_identifier = request.user.id
    if request.method == 'POST':
        try:
            supplier = Supplier.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
            forms = SupplierForm(request.POST)
            if forms.is_valid():
                try:
                    supplier.supplier_name = forms.cleaned_data['supplier_name']
                    supplier.company_name = forms.cleaned_data['company_name']
                    supplier.address = forms.cleaned_data['address']
                    supplier.email = forms.cleaned_data['email']
                    supplier.contact_number = forms.cleaned_data['contact_number']
                    supplier.lead_time = forms.cleaned_data['lead_time']
                    supplier.notes = forms.cleaned_data['notes']
                    supplier.website = forms.cleaned_data['website']
                    supplier.category = forms.cleaned_data['category']
                    supplier.contract_expiry = forms.cleaned_data['contract_expiry']
                    supplier.amount_allocated = forms.cleaned_data['amount_allocated']
                    supplier.city = forms.cleaned_data['city']

                    supplier.save()
                    return redirect('supplier-list')
                except IntegrityError as e:
                    forms.add_error(None, 'Input Value must be unique')
        except Supplier.DoesNotExist:
            return HttpResponse("Supplier does not exist", status=404)

    if supplier is None:
        try:
            supplier = Supplier.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
        except Supplier.DoesNotExist:
            return HttpResponse("Supplier does not exist", status=404)

    return render(request, 'partners/update_supplier.html', {'supplier': supplier, 'form': forms})


@login_required(login_url='login')
def delete_supplier(request, id):
    workspace_identifier = request.user.id
    supplier = Supplier.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
    supplier.delete()
    return redirect('supplier-list')


@login_required(login_url='login')
def create_buyer(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            workspace_identifier = request.user.id           
            # Create the Buyer object
            buyer = form.save(commit=False)
            buyer.workspace_identifier = workspace_identifier
            buyer.save()
            return redirect('buyer-list')
    else:
        form = BuyerForm()

    context = {'form': form}
    return render(request, 'partners/create_buyer.html', context) 


@login_required(login_url='login')
def buyer_list(request):
    workspace_identifier = request.user.id
    buyer = Buyer.objects.filter(workspace_identifier=workspace_identifier)
    return render(request, 'partners/buyer_list.html', {'buyer': buyer})


@login_required(login_url='login')
def update_buyer(request, id):
    buyer = None
    forms = BuyerForm()
    workspace_identifier = request.user.id
    if request.method == 'POST':
        try:
            buyer = Buyer.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
            forms = BuyerForm(request.POST)
            if forms.is_valid():
                try:
                    buyer.buyer_name = forms.cleaned_data['buyer_name']
                    buyer.company_name = forms.cleaned_data['company_name']
                    buyer.address = forms.cleaned_data['address']
                    buyer.email = forms.cleaned_data['email']
                    buyer.contact_number = forms.cleaned_data['contact_number']
                    buyer.amount_allocated = forms.cleaned_data['amount_allocated']
                    buyer.notes = forms.cleaned_data['notes']
                    buyer.credit_limit = forms.cleaned_data['credit_limit']
                    buyer.contract_expiry = forms.cleaned_data['contract_expiry']

                    buyer.save()
                    return redirect('buyer-list')
                except IntegrityError as e:
                    forms.add_error(None, 'Input Value must be unique')
        except Buyer.DoesNotExist:
            return HttpResponse("Buyer does not exist", status=404)

    if buyer is None:
        try:
            buyer = Buyer.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
        except Buyer.DoesNotExist:
            return HttpResponse("Buyer does not exist", status=404)

    return render(request, 'partners/update_buyer.html', {'buyer': buyer, 'form': forms})


@login_required(login_url='login')
def delete_buyer(request, id):
    workspace_identifier = request.user.id
    buyer = Buyer.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
    buyer.delete()
    return redirect('buyer-list')


@login_required(login_url='login')  
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            workspace_identifier = request.user.id
            # Create the Customer object
            customer = form.save(commit=False)
            customer.workspace_identifier = workspace_identifier
            customer.save()
            return redirect('customer-list')
    else:
        form = CustomerForm()

    context = {'form': form}
    return render(request, 'partners/create_customer.html', context)


@login_required(login_url='login')
def customer_list(request):
    workspace_identifier = request.user.id
    customer = Customer.objects.filter(workspace_identifier=workspace_identifier)
    return render(request, 'partners/customer_list.html', {'customer': customer})

@login_required(login_url='login')
def update_customer(request, id):
    customer = None
    forms = CustomerForm()
    workspace_identifier = request.user.id
    if request.method == 'POST':
        try:
            customer = Customer.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
            forms = CustomerForm(request.POST)
            if forms.is_valid():
                try:
                    customer.customer_name = forms.cleaned_data['customer_name']
                    customer.company_name = forms.cleaned_data['company_name']
                    customer.address = forms.cleaned_data['address']
                    customer.email = forms.cleaned_data['email']
                    customer.contact_number = forms.cleaned_data['contact_number']
                    customer.amount_allocated = forms.cleaned_data['amount_allocated']
                    customer.notes = forms.cleaned_data['notes']
                    customer.credit_limit = forms.cleaned_data['credit_limit']
                    customer.contract_expiry = forms.cleaned_data['contract_expiry']

                    customer.save()
                    return redirect('customer-list')
                except IntegrityError as e:
                    forms.add_error(None, 'Input Value must be unique')
        except Customer.DoesNotExist:
            return HttpResponse("Customer does not exist", status=404)

    if customer is None:
        try:
            customer = Customer.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
        except Customer.DoesNotExist:
            return HttpResponse("Customer does not exist", status=404)

    return render(request, 'partners/update_customer.html', {'customer': customer, 'form': forms})


@login_required(login_url='login')
def delete_customer(request, id):
    workspace_identifier = request.user.id
    customer = Customer.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
    customer.delete()
    return redirect('customer-list')


@login_required(login_url='login')
def create_delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            workspace_identifier = request.user.id
            # Create the Delivery object
            delivery = form.save(commit=False)
            delivery.workspace_identifier = workspace_identifier
            delivery.save()
            return redirect('delivery-list')
    else:
        form = DeliveryForm()

    context = {'form': form}
    return render(request, 'partners/create_delivery.html', context)


@login_required(login_url='login')
def delivery_list(request):
    workspace_identifier = request.user.id
    delivery = Delivery.objects.filter(workspace_identifier=workspace_identifier)
    return render(request, 'partners/delivery_list.html', {'delivery': delivery})


@login_required(login_url='login')
def update_delivery(request, id):
    delivery = None
    forms = DeliveryForm()
    workspace_identifier = request.user.id
    if request.method == 'POST':
        try:
            delivery = Delivery.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
            forms = DeliveryForm(request.POST)
            if forms.is_valid():
                try:
                    delivery.delivery_name = forms.cleaned_data['delivery_name']
                    delivery.email = forms.cleaned_data['email']
                    delivery.contact_number = forms.cleaned_data['contact_number']
                    delivery.partner_type = forms.cleaned_data['partner_type']
                    delivery.area_coverage = forms.cleaned_data['area_coverage']
                    delivery.shipping_rates = forms.cleaned_data['shipping_rates']
                    delivery.manager_name = forms.cleaned_data['manager_name']
                    delivery.contract_expiry = forms.cleaned_data['contract_expiry']
                    delivery.notes = forms.cleaned_data['notes']

                    delivery.save()
                    return redirect('delivery-list')
                except IntegrityError as e:
                    forms.add_error(None, 'Input Value must be unique')
        except Delivery.DoesNotExist:
            return HttpResponse("Delivery does not exist", status=404)

    if delivery is None:
        try:
            delivery = Delivery.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
        except Delivery.DoesNotExist:
            return HttpResponse("Delivery does not exist", status=404)

    return render(request, 'partners/update_delivery.html', {'delivery': delivery, 'form': forms})


@login_required(login_url='login')
def delete_delivery(request, id):
    workspace_identifier = request.user.id
    delivery = Delivery.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
    delivery.delete()
    return redirect('delivery-list')