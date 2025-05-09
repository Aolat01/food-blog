from django.shortcuts import render, redirect , get_object_or_404
from .models import myshop
# Create your views here.

def signin(request):
    if request.method =='POST':
        print(request.POST)
        title = request.POST.get('title')
        description = request.POST.get('description')
        print(title, description)

        myshop.objects.create(
            title= title,
            description = description
        )

        return redirect('home')
    
    return render(request, template_name='addpayment.html')


def shoplist(request):
    myshops = myshop.objects.all()
    return render(request, template_name='shopinglist.html', context={"myshops":myshops})

def editmyshop(request,myshop_id):
    myshops = get_object_or_404(myshop , id = myshop_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description') 

        myshops.title= title
        myshops.description = description

        myshops.save()

        return redirect('home')

    else:
        return render(request, template_name='editMyshop.html', context={"myshop":myshops})


def deleteMyshop(request, myshop_id):
    myshops = get_object_or_404(myshop , id = myshop_id)
    myshops.delete()

    return redirect ('YourList')

def handleComplete(request, myshop_id):
    myshops = get_object_or_404(myshop, id = myshop_id)

    myshops.complete_payment = not myshops.complete_payment
    myshops.save()

    return redirect('YourList')