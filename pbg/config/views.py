from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger


def main(request):
    return render(request, 'main.html')


def burger_list(request):
    burgers = Burger.objects.all()
    context = {
        'burgers': burgers
    }
    return render(request, 'burger_list.html', context)


def burger_search(request):
    message = ''
    keyword = request.GET.get('keyword')

    if keyword is not None and len(keyword) > 0:
        burgers = Burger.objects.filter(name__icontains=keyword)
    else:
        burgers = Burger.objects.all()
        message = 'Burgers not found'

    context = {
        'burgers': burgers,
        'message': message
    }
    return render(request, 'burger_search.html', context)