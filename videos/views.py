from django.shortcuts import render


def videos(request):
    """ a view for the videos page """
    template = 'prognosis/videos.html'
    context = {
        'title': 'videos'
    }
    return render(request, template, context)


def controversies_in_prediction_modeling(request):
    """ a view for the controversies in prediction modeling page """
    template = 'prognosis/controversies_in_prediction_modeling.html'
    context = {
        'title': 'controversies in prediction modeling'
    }
    return render(request, template, context)


def covid19_prediction_models(request):
    """ a view for the covid19 prediction models page """
    template = 'prognosis/covid19_prediction_models.html'
    context = {
        'title': 'covid19 prediction models'
    }
    return render(request, template, context)


def emerging_topics_in_prediction_modeling(request):
    """ a view for the emerging topics in prediction modeling page """
    template = 'prognosis/emerging_topics_in_prediction_modeling.html'
    context = {
        'title': 'emerging topics in prediction modeling'
    }
    return render(request, template, context)


def ipd_meta_analysis(request):
    """ a view for the ipd meta analysis page """
    template = 'prognosis/ipd_meta_analysis.html'
    context = {
        'title': 'ipd meta analysis'
    }
    return render(request, template, context)


def penalisation_and_shrinkage(request):
    """ a view for the penalisation and shrinkage page """
    template = 'prognosis/penalisation_and_shrinkage.html'
    context = {
        'title': 'penalisation and shrinkage'
    }
    return render(request, template, context)


def reporting_and_quality(request):
    """ a view for the reporting and quality page """
    template = 'prognosis/reporting_and_quality.html'
    context = {
        'title': 'reporting and quality'
    }
    return render(request, template, context)


def sample_size_for_prediction_modeling(request):
    """ a view for the sample size for prediction modelling page """
    template = 'prognosis/sample_size_for_prediction_modelling.html'
    context = {
        'title': 'sample size for prediction modelling'
    }
    return render(request, template, context)


def systematic_reviews(request):
    """ a view for the systematic reviews page """
    template = 'prognosis/systematic_reviews.html'
    context = {
        'title': 'systematic reviews'
    }
    return render(request, template, context)
