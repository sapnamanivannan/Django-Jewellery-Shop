from django.shortcuts import render
from django.urls import reverse_lazy
from .models import CarouselImage
from products.models import Product

# Create your views here.
def homeView(request):
    template_name = 'mainapp/home.html'
    context = {
        # dictionary with context data.
        'carousel_images' : CarouselImage.objects.all(),
        'products' : Product.objects.all()
        #The above line is equivalent to 'SELECT * FROM CarouselImage;
    }
    return render(request, template_name,context)

# Let's implement CRUD operations for Carousel Image using Class based views.

# Class Based Views are declarative methods to implement views.
# Because of OOPs, the programming style is very abstract i.e., implementation details
# are hidden. 
# These views, even though less detailed in readability, improves abstraction and 
# prevents Re-inventing the wheel, as classes can be inherited and their functionalities
# extended.
    # In Django, realizing the most common usages of request-response scenarios,
    # generic Class Based Views (CBVs) were created.
    # For Inserting new records of the given model into DB, 
        # 1. CreateView (Create)
    # For Querying all records of the given model from DB,
        # 2. ListView   (Read)
    # For Querying a specific record from the given model using pk,
        # 3. DetailView (Read)
    # For Updating or editing a specific record using pk,
        # 4. UpdateView (Update)
    # For Deleting a specific record using pk,
        # 5. DeleteView (Delete)
# ------------------

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

class AddCarouselImage(CreateView):
    model = CarouselImage
    fields = '__all__'
    # context_object_name = 'carousel_images'
    success_url = reverse_lazy('carousel_page')
    template_name = 'mainapp/add_carousel.html' 

#Reading
class ViewCarouselImages(ListView):
    model = CarouselImage
    context_object_name = 'carousel_images'
    template_name = 'mainapp/carousel_list.html'

#Updating
class EditCarousel(UpdateView):
    model = CarouselImage
    template_name = 'mainapp/edit_carousel.html'
    fields = '__all__'
    success_url = reverse_lazy('carousel_page')

# Delete
class RemoveCarousel(DeleteView):
    model = CarouselImage
    template_name = 'mainapp/del_carousel.html'
    success_url = reverse_lazy('carousel_page')

#-----------------------------------

def aboutView(request):
    template_name = 'mainapp/about.html'
    context = {
        # dictionary with context data.
    }
    return render(request, template_name,context)

def contactView(request):
    template_name = 'mainapp/contact.html'
    context = {
        # dictionary with context data.
    }
    return render(request, template_name,context)