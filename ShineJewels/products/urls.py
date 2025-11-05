from django.urls import path

from .views import (ViewProducts, AddProduct,ProductDetail,EditProduct,RemoveProduct)

from.views import EditProductImage,DelProductImage
urlpatterns = [
    path('', ViewProducts.as_view(), name= 'view_products'),
    path('add/', AddProduct.as_view(), name = 'add_product'),
    path('<int:pk>/', ProductDetail.as_view(), name='prod_detail'),
    path('edit/<int:pk>/',EditProduct.as_view(), name='edit_product'),
    path('del/<int:pk>/',RemoveProduct.as_view(), name='del_product'),


    path('iamge/edit/<int:pk>/', EditProductImage.as_view(), name='edit_product_image'),
    path('image/del/<int:pk>/',DelProductImage.as_view(), name='del_product_image')
]