from django.shortcuts import render


def whats_new(request):
    """ a view to display the whats new page """
    template = 'whats_new/whats_new.html'
    context = {
        'title': "what's new?"
    }
    return render(request, template, context)


def latest_research(request):
    """ a view to display the whats new page """
    template = 'whats_new/latest_research.html'
    context = {
        'title': "latest research"
    }
    return render(request, template, context)


def site_updates_log(request):
    """ a view to display the whats new page """
    template = 'whats_new/site_updates_log.html'
    context = {
        'title': "site updates log"
    }
    return render(request, template, context)
