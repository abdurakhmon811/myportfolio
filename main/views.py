from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import render
from os.path import exists
from .foreign_keys import Education, \
    Language, \
    ProgrammingLanguage, \
    WorkExperience
from .metropolis import qrcode_maker, Translator
from .models import About, \
    ContactDetail, \
    Project
from .serializers import AboutSerializer, \
    ContactDetailSerializer, \
    EducationSerializer, \
    LanguageSerializer, \
    ProgrammingLanguageSerializer, \
    ProjectSerializer, \
    WorkExperienceSerializer


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

    translator = Translator()

    request_is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if request_is_ajax and request.method == 'GET' and 'searching_for' in request.GET:
        searching_for = request.GET.get('searching_for')
        if searching_for and len(searching_for) > 0:
            personal_information = About.objects.filter(
            Q(full_bio__icontains=searching_for) |
            Q(skills__icontains=searching_for) |
            Q(hobbies__icontains=searching_for)
            )
            work_experience = WorkExperience.objects.filter(
                Q(work_place__icontains=searching_for) |
                Q(as_a__icontains=searching_for) |
                Q(employment_type__work_type__icontains=searching_for) |
                Q(comment__icontains=searching_for)
            )
            education = Education.objects.filter(
                Q(education__degree__icontains=searching_for) |
                Q(institution__icontains=searching_for) |
                Q(faculty__icontains=searching_for) |
                Q(major__icontains=searching_for) |
                Q(comment__icontains=searching_for)
            )
            languages = Language.objects.filter(
                Q(language__icontains=searching_for) |
                Q(knowledge_extent__icontains=searching_for) |
                Q(comment__icontains=searching_for)
            )
            programming_languages = ProgrammingLanguage.objects.filter(
                Q(language__icontains=searching_for) |
                Q(comment__icontains=searching_for)
            )
            my_projects = Project.objects.filter(
                Q(project_name__icontains=searching_for) |
                Q(description__icontains=searching_for)
            )
            contact_information = ContactDetail.objects.filter(
                Q(media__media_type__icontains=searching_for) |
                Q(comment__icontains=searching_for)
            )
            not_found = None
            if (
                not personal_information and not work_experience and not education and not languages
                and not programming_languages and not my_projects and not contact_information
            ):
                not_found = True
            else:
                not_found = False

            personal_information = AboutSerializer(personal_information, many=True)
            work_experience = WorkExperienceSerializer(work_experience, many=True)
            education = EducationSerializer(education, many=True)
            languages = LanguageSerializer(languages, many=True)
            programming_languages = ProgrammingLanguageSerializer(programming_languages, many=True)
            my_projects = ProjectSerializer(my_projects, many=True)
            contact_information = ContactDetailSerializer(contact_information, many=True)
            context = {
                'searching_for': searching_for,
                'not_found': not_found,
                'resulting_lookup': translator.find_related_words(searching_for, 'media/csv/related_words.csv'),
                'personal_information': personal_information.data,
                'work_experience': work_experience.data,
                'education': education.data,
                'languages': languages.data,
                'programming_languages': programming_languages.data,
                'my_projects': my_projects.data,
                'contact_information': contact_information.data,
            }
            return JsonResponse(context)
        else:
            return JsonResponse({'searching_for': None})
    else:
        raise Http404


def projects(request: HttpRequest):
    """
    Renders the page for checking my projects.
    """

    own_projects = Project.objects.filter(project_created='My own').order_by('date_finished')
    team_projects = Project.objects.filter(project_created='With team').order_by('date_finished')

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
    
    work_exp_length = [i for i in range(0, len(information.work_experience.all()))] if information else None
    education_length = [i for i in range(0, len(information.education.all()))] if information else None
    languages_length = [i for i in range(0, len(information.languages.all()))] if information else None
    programming_languages_length = [i for i in range(0, len(information.programming_languages.all()))] if information else None

    context = {
        'information': information,
        'work_exp_length': work_exp_length,
        'education_length': education_length,
        'languages_length': languages_length,
        'programming_languages_length': programming_languages_length,
        'skills': skills,
        'hobbies': hobbies,
    }
    return render(request, 'main/about.html', context)


def contact_details(request: HttpRequest):
    """
    Renders the page for checking the information on my contact details.
    """

    details = ContactDetail.objects.all()
    results = []
    for detail in details:
        # The path should be changed to an appropriate one when deploying
        path_to_qr = 'media/images/qrcode_%d.png' % int(detail.id)
        if not exists(path_to_qr):
            qr = qrcode_maker(detail.value, 4, 10, 3, (255, 51, 0), (255, 255, 255))
            qr.save(path_to_qr)
        detail_dict = {
            'id': detail.id,
            'media': detail.media,
            'value': detail.value,
            'qrcode': path_to_qr,
            'comment': detail.comment,
            'is_url': detail.is_url,
            'is_email': detail.is_email,
            'is_phone_number': detail.is_phone_number,
        }
        results.append(detail_dict)
    
    context = {
        'results': results,
    }
    return render(request, 'main/contact_details.html', context)
