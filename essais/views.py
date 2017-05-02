from datetime import datetime

from django.shortcuts import render


def home(request):
    

    return render(request, 'essais/home.html', {'date': datetime.now()})
