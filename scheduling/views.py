from django.shortcuts import render
# from django.views import generic, View
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect


def schedule(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'book-appointment.html', context)
