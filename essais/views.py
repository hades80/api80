from datetime import datetime

from django.shortcuts import render


def home(request):
    pseudo = "Hadesian de la Rochefoucaut"
    nb_chevaux = 5
    return render(request, 'essais/home.html', {'date': datetime.now(),'pseudo' : pseudo})
