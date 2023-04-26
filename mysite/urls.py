"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
#from django.contrib.auth.models import User
from django.urls import path, include
#from rest_framework import routers, serializers, viewsets


#class UserSerializer(serializers.HyperlinkedModelSerializer):

#    class Meta:

#        model = User
#        fields = [
#            '__all__'
#        ]


#class UserViewSet(viewsets.ModelViewSet):

#    queryset = User.objects.all()
#    serializer_class = UserSerializer


#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)

urlpatterns = i18n_patterns(
    path('django-management-system/', admin.site.urls),
    path('', include('main.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_apis')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
