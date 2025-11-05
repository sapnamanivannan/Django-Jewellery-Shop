from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

# Create your views here.
from .models import Product, ProductImage
from django.views.generic import (CreateView, ListView,
                                  DetailView, UpdateView,DeleteView)
#importing custom forms
from .forms import ProductImageForm

#----------------Product CRUD-----------------------
class AddProduct(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products/add_product.html'
    # success_url = reverse_lazy("view_products")

class ViewProducts(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/products.html'

class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_details.html'

    # DetailsView doesn't carry an inbuilt form object.
    # We'll create our own form and pass it as an extra context into the template.

    # Let's create a form object from the custom built ProductImageForm and send it
    # as extra context data . 
    # Django CBV utilizes a method called `get_context_data` to collect context data for 
    # template rendering. Let's override that method.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
            
        context['form'] = ProductImageForm() 
        return context                                   


    def post(self, request, pk):
        this_product = Product.objects.get(id = pk)
        form = ProductImageForm(request.POST, request.FILES)
        this_product_image = form.save(commit=False)
        this_product_image.product = this_product
        this_product_image.save()
        return redirect('prod_detail', pk=pk)

class EditProduct(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'products/edit_product.html'
    # success_url = reverse_lazy('view_products')

class RemoveProduct(DeleteView):
    model = Product
    template_name = 'products/del_product.html'
    success_url = reverse_lazy('view_products')



    #-----------ProductImages------------


class EditProductImage(UpdateView):
    model = ProductImage
    template_name ='products/edit_product_image.html'


class DelProductImage(DeleteView):
    model = ProductImage
    template_name = 'products/del_product_image.html'


    def get_success_url(self):
        product_pk = self.object.product.pk
        return reverse_lazy('prod_detail', kwargs={'pk': product_pk})
    