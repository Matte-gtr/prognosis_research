from django.shortcuts import render
from .models import Latest_Research_Year, Research_Update,\
    Site_Page, Site_Log


def whats_new(request):
    """ a view to display the whats new page """
    template = 'whats_new/whats_new.html'
    context = {
        'title': "what's new?"
    }
    return render(request, template, context)


def latest_research(request):
    """ a view to display the whats new page """
    years = Latest_Research_Year.objects.all().order_by('-year')
    research_updates = Research_Update.objects.all()
    template = 'whats_new/latest_research.html'
    context = {
        'title': "latest research",
        'years': years,
        'updates': research_updates,
    }
    return render(request, template, context)


def site_updates_log(request):
    """ a view to display the whats new page """
    site_logs = Site_Log.objects.all().order_by('-date')
    template = 'whats_new/site_updates_log.html'
    context = {
        'title': "site updates log",
        'site_logs': site_logs,
    }
    return render(request, template, context)
