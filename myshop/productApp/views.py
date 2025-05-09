from django.shortcuts import render, redirect
from .forms import ProductForm

# Create your views here.

def addProductView(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('home')

        return render(request, template_name='productApp/addProduct.html', context={'form':form} )
        
    else:
        form = ProductForm()
        return render(request, template_name='productApp/addProduct.html', context={'form':form})