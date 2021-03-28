from django.shortcuts import render
from .models import Merchant


def home(request):
    context = {
        'merchants': Merchant.objects.all()
    }
    return render(request, 'store/home.html', context)
