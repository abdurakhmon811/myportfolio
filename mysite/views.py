from django.http import HttpRequest
from django.shortcuts import render


def maintenance(request: HttpRequest):
    """
    Renders the page for showing the site is on the development.
    """

    return render(request, 'main/maintenance.html')