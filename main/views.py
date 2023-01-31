from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from django.shortcuts import render
from .models import About, \
    ContactDetail, \
    Project


def index(request: HttpRequest):
    """
    Renders the page for the main page.
    """

    return render(request, 'main/index.html')


def projects(request: HttpRequest):
    """
    Renders the page for checking my projects.
    """

    queryset = Project.objects.all()

    context = {
        'queryset': queryset,
    }
    return render(request, 'main/projects.html', context)


def about(request: HttpRequest):
    """
    Renders the page for checking the information on me.
    """

    queryset = None
    try:
        queryset = About.objects.latest('datetime')
    except ObjectDoesNotExist:
        pass

    context = {
        'queryset': queryset,
    }
    return render(request, 'main/about.html', context)


def contact_details(request: HttpRequest):
    """
    Renders the page for checking the information on my contact details.
    """

    queryset = None
    try:
        queryset = ContactDetail.objects.latest('id')
    except ObjectDoesNotExist:
        pass
    
    context = {
        'queryset': queryset,
    }
    return render(request, 'main/contact_details.html', context)


def statistics(request: HttpRequest):
    """
    Renders the page for checking the statistics related to me for various time periods.
    """

    return render(request, 'main/statistics.html')
