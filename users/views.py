from django.shortcuts import render


def index(request):
    print("request-------------", request)
    return render(request, 'users/index.html')
