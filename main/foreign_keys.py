"""Defines models for Foreign Key relationships."""
from django.db import models


class EducationDegree(models.Model):
    """
    A model for handling education degrees which are going to be related to Education model.
    """

    degree = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.degree


class Education(models.Model):
    """
    A model for handling what education I have.
    """

    education = models.ForeignKey(EducationDegree, on_delete=models.PROTECT, null=True)
    institution = models.CharField(max_length=150)
    faculty = models.CharField(max_length=150)
    major = models.CharField(max_length=200)
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
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('Native', 'Native'),
    ]

    language = models.CharField(max_length=100)
    knowledge_extent = models.CharField(max_length=20, choices=degrees)
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
    
    media_type = models.CharField(max_length=100)
    media_image = models.ImageField(upload_to='images')
    comment = models.TextField(null=True)

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.media_type


class ProgrammingLanguage(models.Model):
    """
    A model for handling what kind of programming languages I know and to what extent.
    """

    language = models.CharField(max_length=100)
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

    work_type = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.work_type


class WorkExperience(models.Model):
    """
    A model for handling what work experience I have.
    """

    work_place = models.CharField(max_length=150)
    as_a = models.CharField(max_length=150)         # EXAMPLE: Full-stack Web Developer
    employment_type = models.ForeignKey(WorkType, on_delete=models.PROTECT, null=True)
    started = models.DateField(auto_now_add=False)  # The date I started working at the specified work place
    still_working = models.BooleanField(default=False)
    ended = models.DateField(auto_now_add=False)    # The date I ended working at the specified work place
    comment = models.TextField()

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.work_place
