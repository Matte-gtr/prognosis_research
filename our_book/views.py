from django.shortcuts import render


def our_book(request):
    """ a view for the our book page """
    template = 'our_book/our_book.html'
    context = {
        'title': 'our book'
    }
    return render(request, template, context)


def scope_and_aims(request):
    """ a view for the scope and aims page """
    template = 'our_book/scope_and_aims.html'
    context = {
        'title': 'scope and aims'
    }
    return render(request, template, context)


def table_of_contents(request):
    """ a view for the table of contents page """
    template = 'our_book/table_of_contents.html'
    context = {
        'title': 'table of contents'
    }
    return render(request, template, context)


def about_the_editors(request):
    """ a view for the about the editors page """
    template = 'our_book/about_the_editors.html'
    context = {
        'title': 'about the editors'
    }
    return render(request, template, context)
