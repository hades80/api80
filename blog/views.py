from django.shortcuts import render
from datetime import datetime
# Create your views here.

def home(request):

    return render(request, 'blog/date.html', {'date': datetime.now()})
