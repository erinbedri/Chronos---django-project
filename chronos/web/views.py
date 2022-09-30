from django.shortcuts import render


def show_homepage(request):
    return render(request, 'index.html')
