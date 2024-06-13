from django.shortcuts import render


def index(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'index.html', context)
