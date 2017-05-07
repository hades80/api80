from datetime import datetime

from django.shortcuts import render


def home(request):
    pseudo = "Hadesian de la Rochefoucaut"
    nb_chevaux = 5
    return render(request, 'main/home.html', locals())
