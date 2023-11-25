from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'blog/index.html', context)


def about(request):
    context = {}
    return render(request, 'blog/about.html', context)