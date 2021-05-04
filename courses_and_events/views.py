from django.shortcuts import render


def courses_and_events(request):
    """ a view for the courses and events page """
    template = 'courses_and_events/courses_and_events.html'
    context = {
        'title': 'courses and events'
    }
    return render(request, template, context)


def training_courses(request):
    """ a view for the training courses page """
    template = 'courses_and_events/training_courses.html'
    context = {
        'title': 'training courses'
    }
    return render(request, template, context)


def conferences(request):
    """ a view for the conferences page """
    template = 'courses_and_events/conferences.html'
    context = {
        'title': 'conferences'
    }
    return render(request, template, context)
