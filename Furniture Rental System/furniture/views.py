"""
Views for the Furniture app.

Handles requests related to furniture item listings, details, and seller dashboard.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import FurnitureItem
from .forms import FurnitureItemForm


def item_list(request):
    """
    Displays a list of all furniture items.
    """
    items = FurnitureItem.objects.all()  # pylint: disable=no-member
    return render(request, 'furniture/item_list.html', {'items': items})


def item_detail(request, item_id):
    """
    Displays details of a specific furniture item.
    """
    item = get_object_or_404(FurnitureItem, id=item_id)
    return render(request, 'furniture/item_detail.html', {'item': item})


def index(request):
    """
    Displays the index page.
    """
    return render(request, 'furniture/index.html')


def login_as_buyer(_request):
    """
    Redirects to the item list page for buyers.
    """
    return redirect('item_list')


def login_as_seller(_request):
    """
    Redirects to the seller's dashboard.
    """
    return redirect('seller_dashboard')


def checkout(request, item_id):
    """
    Handles the checkout process for a specific furniture item.
    """
    item = get_object_or_404(FurnitureItem, id=item_id)
    if request.method == 'POST':
        return render(request, 'furniture/checkout_success.html', {'item': item})

    return render(request, 'furniture/buy_item.html', {'item': item})


def checkout_success(request):
    """
    Displays the checkout success page.
    """
    return render(request, 'furniture/checkout_success.html')


@login_required
def add_item(request):
    """
    Allows the seller to add a new furniture item.
    """
    if request.method == 'POST':
        form = FurnitureItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return redirect('seller_dashboard')
    else:
        form = FurnitureItemForm()
    return render(request, 'furniture/add_item.html', {'form': form})


def buy_item(request, item_id):
    """
    Processes the purchase of a furniture item and reduces its quantity.
    """
    item = get_object_or_404(FurnitureItem, id=item_id)
    if item.is_available():
        item.quantity -= 1
        item.save()
    else:
        return render(request,'furniture/item_detail.html',\
        {'item': item, 'error': 'Item not available'})
    return render(request, 'furniture/buy_item.html', {'item': item})


@login_required
def seller_dashboard(request):
    """
    Displays the seller's dashboard with their items and a form to add new items.
    """
    seller_items = FurnitureItem.objects.filter(seller=request.user)  # pylint: disable=no-member
    if request.method == 'POST':
        form = FurnitureItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return redirect('seller_dashboard')
    else:
        form = FurnitureItemForm()

    return render(request, 'furniture/seller_dashboard.html', {'items': seller_items, 'form': form}) # pylint: disable=no-member


@login_required
def edit_item(request, item_id):
    """
    Allows the seller to edit an existing furniture item.
    """
    item = get_object_or_404(FurnitureItem, id=item_id, seller=request.user)
    if request.method == 'POST':
        form = FurnitureItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    else:
        form = FurnitureItemForm(instance=item)
    return render(request, 'furniture/edit_item.html', {'form': form})


@login_required
def delete_item(request, item_id):
    """
    Allows the seller to delete a furniture item.
    """
    item = get_object_or_404(FurnitureItem, id=item_id, seller=request.user)
    item.delete()
    return redirect('seller_dashboard')


def signup(request):
    """
    Handles user signup and redirects to the item list upon success.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('item_list')
    else:
        form = UserCreationForm()
    return render(request, 'furniture/signup.html', {'form': form})


def rent_item(request, item_id):
    """
    Displays the rent item page.
    """
    item = get_object_or_404(FurnitureItem, id=item_id)
    return render(request, 'furniture/rent_item.html', {'item': item})


@login_required
def seller_items(request):
    """
    Displays a list of items added by the current seller.
    """
    items = FurnitureItem.objects.filter(seller=request.user) # pylint: disable=no-member
    return render(request, 'furniture/seller_items.html', {'items': items})
