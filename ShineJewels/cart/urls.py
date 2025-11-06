from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewCart, name='view_cart'),
    path('add/<int:product_id>', views.addToCart, name='add_to_cart'),
    path('remove/<int:cart_item_id>', views.remFromCart, name = 'rem_from_cart'),
            # The following url patterns will be requested by the JS function
    path('add/q/<int:cart_item_id>', views.addQuantity, name='add_quantity'),
    path('remove/q/<int:cart_item_id>', views.remQuantity, name='rem_quantity'),

]