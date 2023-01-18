from django.shortcuts import render


def index(request):
    """
    Renders the page for the main page.
    """

    return render(request, 'main/index.html')
