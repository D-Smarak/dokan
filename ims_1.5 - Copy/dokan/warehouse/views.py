from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import IntegrityError
from django.forms import ModelForm
from users.models import CustomUser
from .models import Drop, Product, Category, Stock
from .forms import DropForm, ProductForm, CategoryForm, StockForm


# Drop views
@login_required(login_url='login')
def create_drop(request):
    if request.method == 'POST':
        form = DropForm(request.POST)
        if form.is_valid():
            # Retrieve the workspace identifier of the current user
            workspace_identifier = request.user.id
            
            # Create the Drop object
            drop = form.save(commit=False)
            drop.workspace_identifier = workspace_identifier
            drop.save()
            return redirect('drop-list')
    else:
        form = DropForm()

    context = {'form': form}
    return render(request, 'warehouse/create_drop.html', context)

@login_required(login_url='login')
def drop_list(request):
    workspace_identifier = request.user.id
    drop = Drop.objects.filter(workspace_identifier=workspace_identifier)
    return render(request, 'warehouse/drop_list.html', {'drop': drop})

@login_required(login_url='login')
def update_drop(request, id):
    drop = None
    forms = DropForm()
    workspace_identifier = request.user.id
    if request.method == 'POST':
        try:
            drop = Drop.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
            forms = DropForm(request.POST)
            if forms.is_valid():
                try:
                    drop.name = forms.cleaned_data['name']
                    drop.address = forms.cleaned_data['address']
                    drop.city = forms.cleaned_data['city']
                    drop.postal_code = forms.cleaned_data['postal_code']
                    drop.email = forms.cleaned_data['email']
                    drop.contact_person = forms.cleaned_data['contact_person']
                    drop.contact_number = forms.cleaned_data['contact_number']
                    drop.notes = forms.cleaned_data['notes']
                    drop.state = forms.cleaned_data['state']
                    drop.country = forms.cleaned_data['country']
                    drop.capacity = forms.cleaned_data['capacity']
                    drop.available_space = forms.cleaned_data['available_space']
                    drop.used_space = forms.cleaned_data['used_space']

                    drop.save()
                    return redirect('drop-list')
                except IntegrityError as e:
                    forms.add_error(None, 'Input Value must be unique')
        except Drop.DoesNotExist:
            return HttpResponse("Drop does not exist", status=404)

    if drop is None:
        try:
            drop = Drop.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
        except Drop.DoesNotExist:
            return HttpResponse("Drop does not exist", status=404)

    return render(request, 'warehouse/update_drop.html', {'drop': drop, 'form': forms})

@login_required(login_url='login')
def delete_drop(request, id):
    workspace_identifier = request.user.id
    drop = Drop.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
    drop.delete()
    return redirect('drop-list')


# Product views
@login_required(login_url='login')
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Retrieve the workspace identifier of the current user
            workspace_identifier = request.user.id
            
            # Create the Product object
            product = form.save(commit=False)
            product.workspace_identifier = workspace_identifier
            product.save()
            return redirect('product-list')
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'warehouse/create_product.html', context)


@login_required(login_url='login')
def product_list(request):
    workspace_identifier = request.user.id
    product = Product.objects.filter(workspace_identifier=workspace_identifier)
    return render(request, 'warehouse/product_list.html', {'product': product})


@login_required(login_url='login')
def update_product(request, id):
    product = None
    forms = ProductForm()
    workspace_identifier = request.user.id
    if request.method == 'POST':
        try:
            product = Product.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
            forms = ProductForm(request.POST)
            if forms.is_valid():
                try:
                    product.name = forms.cleaned_data['name']
                    product.description = forms.cleaned_data['description']
                    product.manufacture_date = forms.cleaned_data['manufacture_date']
                    product.brand = forms.cleaned_data['brand']
                    product.category = forms.cleaned_data['category']
                    product.model_number = forms.cleaned_data['model_number']
                    product.barcode_number = forms.cleaned_data['barcode_number']
                    product.price = forms.cleaned_data['price']
                    product.sortno = forms.cleaned_data['sortno']
                    product.quantity = forms.cleaned_data['quantity']
                    product.unit_of_measurement = forms.cleaned_data['unit_of_measurement']
                    product.cost_price = forms.cleaned_data['cost_price']
                    product.selling_price = forms.cleaned_data['selling_price']
                    product.weight = forms.cleaned_data['weight']
                    product.dimensions = forms.cleaned_data['dimensions']
                    product.expiry_date = forms.cleaned_data['expiry_date']
                    product.barcode = forms.cleaned_data['barcode']
                    product.product_image = forms.cleaned_data['product_image']
                    product.stock_count = forms.cleaned_data['stock_count']

                    product.save()
                    return redirect('product-list')
                except IntegrityError as e:
                    forms.add_error(None, 'Input Value must be unique')
        except Product.DoesNotExist:
            return HttpResponse("Product does not exist", status=404)

    if product is None:
        try:
            product = Product.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
        except Product.DoesNotExist:
            return HttpResponse("Product does not exist", status=404)

    return render(request, 'warehouse/update_product.html', {'product': product, 'form': forms})

@login_required(login_url='login')
def delete_product(request, id):
    workspace_identifier = request.user.id
    product = Product.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
    product.delete()
    return redirect('product-list')



# Category views
@login_required(login_url='login')
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # Retrieve the workspace identifier of the current user
            workspace_identifier = request.user.id
            
            # Create the Category object
            category = form.save(commit=False)
            category.workspace_identifier = workspace_identifier
            category.save()
            return redirect('category-list')
    else:
        form = CategoryForm()

    context = {'form': form}
    return render(request, 'warehouse/create_category.html', context)


@login_required(login_url='login')
def category_list(request):
    workspace_identifier = request.user.id
    category = Category.objects.filter(workspace_identifier=workspace_identifier)
    return render(request, 'warehouse/category_list.html', {'category': category})

@login_required(login_url='login')
def update_category(request, id):
    category = None
    forms = CategoryForm()
    workspace_identifier = request.user.id
    if request.method == 'POST':
        try:
            category = Category.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
            forms = CategoryForm(request.POST)
            if forms.is_valid():
                try:
                    category.name = forms.cleaned_data['name']
                    category.description = forms.cleaned_data['description']
                    category.parent = forms.cleaned_data['parent']
                    category.code = forms.cleaned_data['code']
                    category.category_image = forms.cleaned_data['category_image']
                    category.stock_count = forms.cleaned_data['stock_count']
                    category.sales_margin = forms.cleaned_data['sales_margin']
                    category.associated_products = forms.cleaned_data['associated_products']
                    category.notes = forms.cleaned_data['notes']

                    category.save()
                    return redirect('category-list')
                except IntegrityError as e:
                    forms.add_error(None, 'Input Value must be unique')
        except Category.DoesNotExist:
            return HttpResponse("Category does not exist", status=404)

    if category is None:
        try:
            category = Category.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
        except Category.DoesNotExist:
            return HttpResponse("Category does not exist", status=404)

    return render(request, 'warehouse/update_category.html', {'category': category, 'form': forms})

@login_required(login_url='login')
def delete_category(request, id):
    workspace_identifier = request.user.id
    category = Category.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
    category.delete()
    return redirect('category-list')



# Stock views
@login_required(login_url='login')
def create_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            # Retrieve the workspace identifier of the current user
            workspace_identifier = request.user.id
            
            # Create the Stock object
            stock = form.save(commit=False)
            stock.workspace_identifier = workspace_identifier
            stock.save()
            return redirect('stock-list')
    else:
        form = StockForm()

    context = {'form': form}
    return render(request, 'warehouse/create_stock.html', context)

@login_required(login_url='login')
def stock_list(request):
    workspace_identifier = request.user.id
    stock = Stock.objects.filter(workspace_identifier=workspace_identifier)
    return render(request, 'warehouse/stock_list.html', {'stock': stock})

@login_required(login_url='login')
def update_stock(request, id):
    stock = None
    forms = StockForm()
    workspace_identifier = request.user.id
    if request.method == 'POST':
        try:
            stock = Stock.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
            forms = StockForm(request.POST)
            if forms.is_valid():
                try:
                    stock.product = forms.cleaned_data['product']
                    stock.drop = forms.cleaned_data['drop']
                    stock.quantity = forms.cleaned_data['quantity']
                    stock.unit_of_measurement = forms.cleaned_data['unit_of_measurement']
                    stock.cost_price = forms.cleaned_data['cost_price']
                    stock.selling_price = forms.cleaned_data['selling_price']
                    stock.weight = forms.cleaned_data['weight']
                    stock.dimensions = forms.cleaned_data['dimensions']
                    stock.expiry_date = forms.cleaned_data['expiry_date']

                    stock.save()
                    return redirect('stock-list')
                except IntegrityError as e:
                    forms.add_error(None, 'Input Value must be unique')
        except Stock.DoesNotExist:
            return HttpResponse("Stock does not exist", status=404)

    if stock is None:
        try:
            stock = Stock.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
        except Stock.DoesNotExist:
            return HttpResponse("Stock does not exist", status=404)

    return render(request, 'warehouse/update_stock.html', {'stock': stock, 'form': forms})


@login_required(login_url='login')
def delete_stock(request, id):
    workspace_identifier = request.user.id
    stock = Stock.objects.filter(workspace_identifier=workspace_identifier, id=id).first()
    stock.delete()
    return redirect('stock-list')
