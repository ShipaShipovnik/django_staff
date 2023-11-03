from django.shortcuts import render, redirect
from .models import Staff
from .forms import StaffForm


def index(request):
    staff = Staff.objects.all
    return render(request, 'main/index.html', {'staff': staff})


def about(request):
    return render(request, 'main/about.html')


def addstaff(request):
    error = ""
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = StaffForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/addstaff.html', context)

