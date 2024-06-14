from django.shortcuts import render


def index(request):

    print("request-------------", request)
    return render(request, 'users/index.html')

    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'index.html', context)


def patient(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'patient.html', context)

