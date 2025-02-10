from django.shortcuts import get_object_or_404, render
from .models import Item

# return 404 if item's details  isn't available. 
def detail(request,pk): #pk==primary-key
    item = get_object_or_404(Item, pk=pk)

    return render (request, "item/detail.html",{
        "item": item
    })

