from django.shortcuts import render


def home(request):
    """ a view to display the home page """
    template = 'home/index.html'
    context = {
        'title': 'home',
    }
    return render(request, template, context)
