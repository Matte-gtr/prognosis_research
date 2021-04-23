from django.shortcuts import render


def prognosis(request):
    """ a view for the Prognosis page """
    template = 'prognosis/prognosis.html'
    context = {
        'title': 'prognosis'
    }
    return render(request, template, context)


def video_introduction(request):
    """ a view for the video introduction page """
    template = 'prognosis/video_introduction.html'
    context = {
        'title': 'video introduction'
    }
    return render(request, template, context)


def what_is_prognosis(request):
    """ a view for the what is prognosis page """
    template = 'prognosis/what_is_prognosis.html'
    context = {
        'title': 'what is prognosis'
    }
    return render(request, template, context)


def what_is_prognosis_research(request):
    """ a view for the what is prognosis research page """
    template = 'prognosis/what_is_prognosis_research.html'
    context = {
        'title': 'what is prognosis research'
    }
    return render(request, template, context)


def the_progress_framework(request):
    """ a view for the progress framework page """
    template = 'prognosis/the_progress_framework.html'
    context = {
        'title': 'the progress framework'
    }
    return render(request, template, context)


def quotes_of_note(request):
    """ a view for the quotes of note page """
    template = 'prognosis/quotes_of_note.html'
    context = {
        'title': 'quotes of note'
    }
    return render(request, template, context)
