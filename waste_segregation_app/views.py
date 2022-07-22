from django.shortcuts import render, redirect

from .models import Trash
from .forms import TrashForm
# Create your views here.

def new_trash(request):
    if request.method != 'POST':
        form = TrashForm()
    else:
        form = TrashForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('waste_segregation_app:bin')
    context = {'form': form}
    return render(request, 'waste_segregation_app/new_trash.html', context)

def check_bin(request):
    trash = Trash.objects.last()
    bin = trash.check_bin()
    
    context = {'bin':bin}
    return render (request, 'waste_segregation_app/bin.html', context)
    
