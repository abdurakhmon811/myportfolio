"""Defines models for Foreign Key relationships."""
from django.db import models


class EducationDegree(models.Model):
    """
    A model for handling education degrees which are going to be related to Education model.
    """

    degree = models.CharField(max_length=150)

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.degree


class Education(models.Model):
    """
    A model for handling what education I have.
    """

    education = models.ForeignKey(EducationDegree, on_delete=models.PROTECT, null=True)
    institution = models.CharField(max_length=600)
    faculty = models.CharField(max_length=400)
    major = models.CharField(max_length=400)
    start_date = models.DateField(auto_now_add=False)
    still_studying = models.BooleanField(default=False)
    end_date = models.DateField(auto_now_add=False, null=True)
    comment = models.TextField(null=True)

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.institution


class Language(models.Model):
    """
    A model for handling what speaking languages I know and to what extent.
    """

    degrees = [
        (
            '--de A1 ||| --en A1 ||| --ru A1 ||| --uz A1', 
            '--de A1 ||| --en A1 ||| --ru A1 ||| --uz A1',
        ),
        (
            '--de A2 ||| --en A2 ||| --ru A2 ||| --uz A2', 
            '--de A2 ||| --en A2 ||| --ru A2 ||| --uz A2',
        ),
        (
            '--de B1 ||| --en B1 ||| --ru B1 ||| --uz B1', 
            '--de B1 ||| --en B1 ||| --ru B1 ||| --uz B1',
        ),
        (
            '--de B2 ||| --en B2 ||| --ru B2 ||| --uz B2', 
            '--de B2 ||| --en B2 ||| --ru B2 ||| --uz B2',
        ),
        (
            '--de C1 ||| --en C1 ||| --ru C1 ||| --uz C1', 
            '--de C1 ||| --en C1 ||| --ru C1 ||| --uz C1',
        ),
        (
            '--de Einheimisch ||| --en Native ||| --ru Родной ||| --uz Mahalliy', 
            '--de Einheimisch ||| --en Native ||| --ru Родной ||| --uz Mahalliy',
        ),
    ]

    language = models.CharField(max_length=200)
    knowledge_extent = models.CharField(max_length=70, choices=degrees)
    comment = models.TextField(null=True)

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.language


class Media(models.Model):
    """"
    A model for handling the type of social media.
    """

    class Meta:

        verbose_name = 'Media'
        verbose_name_plural = 'Media'
    
    media_type = models.CharField(max_length=150)
    media_image = models.ImageField(upload_to='images')

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.media_type


class ProgrammingLanguage(models.Model):
    """
    A model for handling what kind of programming languages I know and to what extent.
    """

    language = models.CharField(max_length=200)
    started = models.DateField(auto_now_add=False)      # The date when I started learning programming
    still_learning = models.BooleanField(default=True)
    ended = models.DateField(auto_now_add=False, null=True)
    comment = models.TextField(null=True)                     # What I can do using the language

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.language


class WorkType(models.Model):
    """
    A model for handling work types which are going to be related to WorkExperience model.
    """

    work_type = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.work_type


class WorkExperience(models.Model):
    """
    A model for handling what work experience I have.
    """

    work_place = models.CharField(max_length=200)
    as_a = models.CharField(max_length=200)         # EXAMPLE: Full-stack Web Developer
    employment_type = models.ForeignKey(WorkType, on_delete=models.PROTECT, null=True)
    started = models.DateField(auto_now_add=False)  # The date I started working at the specified work place
    still_working = models.BooleanField(default=False)
    ended = models.DateField(auto_now_add=False)    # The date I ended working at the specified work place
    comment = models.TextField()

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.work_place
