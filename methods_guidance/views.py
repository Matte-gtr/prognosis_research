from django.shortcuts import render


def methods_guidance(request):
    """ a view for the methods guidance page """
    template = 'methods_guidance/methods_guidance.html'
    context = {
        'title': 'methods guidance'
    }
    return render(request, template, context)


def progress_series(request):
    """ a view for the progress series page """
    template = 'methods_guidance/progress_series.html'
    context = {
        'title': 'progress series'
    }
    return render(request, template, context)


def prognostic_factors(request):
    """ a view for the prognostic factors page """
    template = 'methods_guidance/prognostic_factors.html'
    context = {
        'title': 'prognostic factors'
    }
    return render(request, template, context)


def prognostic_models(request):
    """ a view for the prognostic models page """
    template = 'methods_guidance/prognostic_models.html'
    context = {
        'title': 'prognostic models'
    }
    return render(request, template, context)


def systematic_reviews_and_meta_analysis(request):
    """ a view for the systematic reviews and meta-analysis page """
    template = 'methods_guidance/systematic_reviews_and_meta_analysis.html'
    context = {
        'title': 'systematic reviews & meta analysis'
    }
    return render(request, template, context)


def reporting(request):
    """ a view for the reporting page """
    template = 'methods_guidance/reporting.html'
    context = {
        'title': 'reporting'
    }
    return render(request, template, context)


def software_websites_and_apps(request):
    """ a view for the software, websites and apps page """
    template = 'methods_guidance/software_websites_and_apps.html'
    context = {
        'title': 'software, websites & apps'
    }
    return render(request, template, context)


def textbooks(request):
    """ a view for the textbooks page """
    template = 'methods_guidance/textbooks.html'
    context = {
        'title': 'textbooks'
    }
    return render(request, template, context)
