from django.shortcuts import render


def fp(request):
    return render(request, 'cover/fp.html')
