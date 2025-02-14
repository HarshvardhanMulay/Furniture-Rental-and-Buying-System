"""
URL configuration for the furniture app.

Defines URL patterns for the app, including views for buyers, sellers, 
and general item management.
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import item_detail, login_as_buyer, login_as_seller, \
    checkout_success, add_item, rent_item, buy_item
# Removed duplicate direct imports (item_list, index, checkout)

urlpatterns = [
    # Home page and main navigation
    path('', views.index, name='index'), # Index is used, so this import is necessary
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('login_as_buyer/', login_as_buyer, name='login_as_buyer'),
    path('login_as_seller/', login_as_seller, name='login_as_seller'),
    # Items management
    path(
        'items/',
        views.item_list,
        name='item_list'
    ), # item_list is used, so this import is necessary
    path(
        'checkout/<int:item_id>/',
        views.checkout,
        name='checkout'
    ), # checkout is used, so this import is necessary
    path('checkout/success/', checkout_success, name='checkout_success'),
    path('add-item/', add_item, name='add_item'),
    path('item/<int:item_id>/rent/', rent_item, name='rent_item'),
    path('item/<int:item_id>/buy', buy_item, name='buy_item'),
    # Authentication
    path('signup/', views.signup, name='signup'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='index.html',
            next_page='item_list'
            ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='index'),
        name='logout'
    ),
    # Seller dashboard and management
    path('items_list/', views.item_list, name='item_list'),
    path('seller-items/', views.seller_items, name='seller_items'),
    path('seller/dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path(
        'seller/edit/<int:item_id>/',
        views.edit_item,
        name='edit_item'
    ),
    path(
        'seller/delete/<int:item_id>/',
        views.delete_item,
        name='delete_item'
    ),
]
