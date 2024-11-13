# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from myapp.models import TblUser, TblCustomer, TblVendor, TblSalesOrder, TblPurchaseOrder, TblLedger
from .forms import UserForm, CustomerForm, VendorForm, SalesOrderForm, PurchaseOrderForm, LedgerForm
from django.contrib.auth import logout

# Logout function
def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Manually authenticate the user from the TblUser model
            user = TblUser.objects.get(username=username, password=password)  # No hash comparison
            # Set session data manually
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('success_page')  # Redirect to the success page
        except TblUser.DoesNotExist:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

# Read - Display all users
def user_list(request):
    users = TblUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

# Create - Add a new user
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

# Update - Edit an existing user
def user_update(request, id):
    user = get_object_or_404(TblUser, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

def user_detail(request, id):
    user = get_object_or_404(TblUser, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_detail.html', {'form': form})

# Delete - Remove a user
def user_delete(request, id):
    user = get_object_or_404(TblUser, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})

def accounting(request):
    return render(request, 'accounting.html')

def report_view(request):
    return render(request, 'report.html')

def vendor_view(request):
    return render(request, 'vendor.html')

def customer_view(request):
    return render(request, 'customer.html')

def vendor_view(request):
    return render(request, 'vendor.html')

def ledger_view(request):
    return render(request, 'ledger.html')

def customer_list(request):
    customers = TblCustomer.objects.all()  # Assuming you have a TblCustomer model
    return render(request, 'customer.html', {'customers': customers})

def customer_create(request):
    if request.method == 'POST':
        retail_name = request.POST['retail_name']
        address = request.POST['address']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        # Create a new customer instance and save it to the database
        customer = TblCustomer(
            retail_name=retail_name,
            address=address,
            email=email,
            phone_number=phone_number
        )
        customer.save()

        return redirect('customer_list')  # Corrected redirect to the customer list page

    return render(request, 'customer_form.html')  # Show the form

def customer_detail(request, id):
    customer = get_object_or_404(TblCustomer, id=id)
    return render(request, 'customer_detail.html', {'customer': customer})

def customer_update(request, id):
    customer = get_object_or_404(TblCustomer, id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'customer_update.html', {'form': form, 'customer': customer})


def customer_delete(request, id):
    customer = get_object_or_404(TblCustomer, id=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')  # Redirect to the customer list or appropriate page
    return render(request, 'customer_confirm_delete.html', {'customer': customer})

def vendor_list(request):
    vendors = TblVendor.objects.all()  # Assuming you have a TblVendor model
    return render(request, 'vendor.html', {'vendors': vendors})

def vendor_create(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        address = request.POST['address']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        contract_period = request.POST['contract_period']

        # Create a new vendor instance and save it to the database
        vendor = TblVendor(
            company_name=company_name,
            address=address,
            email=email,
            phone_number=phone_number,
            contract_period=contract_period  # Include contract_period
        )
        vendor.save()

        return redirect('vendor_list')  # Corrected redirect to the vendor list page

    return render(request, 'vendor_form.html')  # Show the form

def vendor_detail(request, id):
    vendor = get_object_or_404(TblVendor, id=id)
    return render(request, 'vendor_detail.html', {'vendor': vendor})

def vendor_update(request, id):
    vendor = get_object_or_404(TblVendor, id=id)
    if request.method == "POST":
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm(instance=vendor)

    return render(request, 'vendor_update.html', {'form': form, 'vendor': vendor})

def vendor_delete(request, id):
    vendor = get_object_or_404(TblVendor, id=id)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendor_list')  # Redirect to the vendor list or appropriate page
    return render(request, 'vendor_confirm_delete.html', {'vendor': vendor})

# Read - Display all sales orders
def sales_order_list(request):
    sales_orders = TblSalesOrder.objects.all()
    return render(request, 'sales_order_list.html', {'sales_orders': sales_orders})

# Create - Add a new sales order
def sales_order_create(request):
    if request.method == 'POST':
        form = SalesOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_order_list')
    else:
        form = SalesOrderForm()
    return render(request, 'sales_order_form.html', {'form': form})

# Update - Edit an existing sales order
def sales_order_update(request, id):
    sales_order = get_object_or_404(TblSalesOrder, id=id)
    if request.method == 'POST':
        form = SalesOrderForm(request.POST, instance=sales_order)
        if form.is_valid():
            form.save()
            return redirect('sales_order_list')
    else:
        form = SalesOrderForm(instance=sales_order)
    return render(request, 'sales_order_form.html', {'form': form})

def sales_order_detail(request, id):
    sales_order = get_object_or_404(TblSalesOrder, id=id)
    if request.method == 'POST':
        form = SalesOrderForm(request.POST, instance=sales_order)
        if form.is_valid():
            form.save()
            return redirect('sales_order_list')
    else:
        form = SalesOrderForm(instance=sales_order)
    return render(request, 'sales_order_detail.html', {'form': form})

# Delete - Remove a sales order
def sales_order_delete(request, id):
    sales_order = get_object_or_404(TblSalesOrder, id=id)
    if request.method == 'POST':
        sales_order.delete()
        return redirect('sales_order_list')
    return render(request, 'sales_order_confirm_delete.html', {'sales_order': sales_order})

# Read - Display all sales orders
def purchase_order_list(request):
    purchase_orders = TblPurchaseOrder.objects.all()
    return render(request, 'purchase_order_list.html', {'purchase_orders': purchase_orders})

# Create - Add a new sales order
def purchase_order_create(request):
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_order_list')
    else:
        form = PurchaseOrderForm()
    return render(request, 'purchase_order_form.html', {'form': form})

# Update - Edit an existing sales order
def purchase_order_update(request, id):
    purchase_order = get_object_or_404(TblPurchaseOrder, id=id)
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST, instance=purchase_order)
        if form.is_valid():
            form.save()
            return redirect('purchase_order_list')
    else:
        form = PurchaseOrderForm(instance=purchase_order)
    return render(request, 'purchase_order_form.html', {'form': form})

def purchase_order_detail(request, id):
    purchase_order = get_object_or_404(TblPurchaseOrder, id=id)
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST, instance=purchase_order)
        if form.is_valid():
            form.save()
            return redirect('purchase_order_list')
    else:
        form = PurchaseOrderForm(instance=purchase_order)
    return render(request, 'purchase_order_detail.html', {'form': form})

# Delete - Remove a sales order
def purchase_order_delete(request, id):
    purchase_order = get_object_or_404(TblPurchaseOrder, id=id)
    if request.method == 'POST':
        purchase_order.delete()
        return redirect('purchase_order_list')
    return render(request, 'purchase_order_confirm_delete.html', {'purchase_order': purchase_order})

# Read - Display all sales orders
def ledger_list(request):
    ledger = TblLedger.objects.all()
    return render(request, 'ledger_list.html', {'ledger': ledger})

# Create - Add a new sales order
def ledger_create(request):
    if request.method == 'POST':
        form = LedgerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ledger_list')
    else:
        form = LedgerForm()
    return render(request, 'ledger_form.html', {'form': form})

# Update - Edit an existing sales order
def ledger_update(request, id):
    purchase_order = get_object_or_404(TblLedger, id=id)
    if request.method == 'POST':
        form = LedgerForm(request.POST, instance=purchase_order)
        if form.is_valid():
            form.save()
            return redirect('ledger_list')
    else:
        form = LedgerForm(instance=purchase_order)
    return render(request, 'ledger_form.html', {'form': form})

def ledger_detail(request, id):
    purchase_order = get_object_or_404(TblLedger, id=id)
    if request.method == 'POST':
        form = LedgerForm(request.POST, instance=purchase_order)
        if form.is_valid():
            form.save()
            return redirect('ledger_list')
    else:
        form = LedgerForm(instance=purchase_order)
    return render(request, 'ledger_detail.html', {'form': form})

# Delete - Remove a sales order
def ledger_delete(request, id):
    purchase_order = get_object_or_404(TblLedger, id=id)
    if request.method == 'POST':
        purchase_order.delete()
        return redirect('ledger_list')
    return render(request, 'ledger_confirm_delete.html', {'purchase_order': purchase_order})