from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]

    # Construct a dict to pass to the template as its context
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    # Return a rendered response to send to the cient
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')