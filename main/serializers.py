from rest_framework import serializers
from .foreign_keys import Education, \
    Language, \
    ProgrammingLanguage, \
    WorkExperience
from .models import About, \
    ContactDetail, \
    Project


class AboutSerializer(serializers.ModelSerializer):
    """
    A serializer for converting ABOUT data.
    """

    class Meta:

        model = About
        fields = [
            'full_bio',
            'skills',
            'hobbies',
        ]


class ContactDetailSerializer(serializers.ModelSerializer):
    """
    A serializer for converting CONTACT DETAILS data.
    """

    media = serializers.SlugRelatedField('media_type', read_only=True)

    class Meta:

        model = ContactDetail
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    """
    A serializer for converting EDUCATION data.
    """

    education = serializers.SlugRelatedField('degree', read_only=True)

    class Meta:

        model = Education
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    """
    A serializer for converting LANGUAGE data.
    """

    class Meta:

        model = Language
        fields = '__all__'


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    """
    A serializer for converting PROGRAMMING LANGUAGE data.
    """

    class Meta:

        model = ProgrammingLanguage
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """
    A serializer for converting PROJECT data.
    """

    class Meta:

        model = Project
        fields = '__all__'


class WorkExperienceSerializer(serializers.ModelSerializer):
    """
    A serializer for converting WORK EXPERIENCE data.
    """

    employment_type = serializers.SlugRelatedField('work_type', read_only=True)

    class Meta:

        model = WorkExperience
        fields = '__all__'
