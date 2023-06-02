# en views.py
from django.shortcuts import render


def favoritos(request):

    return render(request, 'favoritos/favoritos.html')
