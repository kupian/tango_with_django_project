from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dict to pass to the template as its context
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return a rendered response to send to the cient
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')