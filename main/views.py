from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render
from .models import About, \
    ContactDetail, \
    Project


def index(request: HttpRequest):
    """
    Renders the page for the main page.
    """

    information = None
    try:
        information = About.objects.latest('datetime')
    except ObjectDoesNotExist:
        pass
    
    context = {
        'information': information,
    }
    return render(request, 'main/index.html', context)


def search(request: HttpRequest):
    """
    Renders the page with the search results.
    """
    
    searched = None
    personal_information = None
    my_projects = None
    contact_information = None

    if request.method == 'GET' and 'searched' in request.GET:
        searched = request.GET.get('searched')
        personal_information = About.objects.filter(Q(title__contains=searched) | 
                                                    Q(full_bio__contains=searched))
        my_projects = Project.objects.filter(Q(project_name__contains=searched) |
                                             Q(description__contains=searched))
        contact_information = ContactDetail.objects.filter(Q(media__contains=searched) |
                                                           Q(comment_contains=searched))
    
    context = {
        'searched': searched,
        'personal_information': personal_information,
        'my_projects': my_projects,
        'contact_information': contact_information,
    }
    return render(request, 'main/search.html', context)


def projects(request: HttpRequest):
    """
    Renders the page for checking my projects.
    """

    own_projects = Project.objects.filter(project_created='My own')
    team_projects = Project.objects.filter(project_created='With team')

    context = {
        'own_projects': own_projects,
        'team_projects': team_projects,
    }
    return render(request, 'main/projects.html', context)


def about(request: HttpRequest):
    """
    Renders the page for checking the information on me.
    """

    information = None
    skills = None
    hobbies = None
    try:
        information = About.objects.latest('datetime')
        skills = information.skills.split(',')
        hobbies = information.hobbies.split(',')
    except ObjectDoesNotExist:
        pass

    context = {
        'information': information,
        'skills': skills,
        'hobbies': hobbies,
    }
    return render(request, 'main/about.html', context)


def contact_details(request: HttpRequest):
    """
    Renders the page for checking the information on my contact details.
    """

    details = None
    try:
        details = ContactDetail.objects.latest('id')
    except ObjectDoesNotExist:
        pass
    
    context = {
        'details': details,
    }
    return render(request, 'main/contact_details.html', context)
