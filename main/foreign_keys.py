"""Defines models for Foreign Key relationships."""
from django.db import models


class Education(models.Model):
    """
    A model for handling what education I have.
    """

    degrees = [
        ('Associate degree', 'Associate degree'),
        ("Bachelor's degree", "Bachelor's degree"),
        ("Master's degree", "Master's degree"),
        ('Doctoral degree', 'Doctoral degree'),
    ]

    education = models.CharField(max_length=100, choices=degrees)
    institution = models.CharField(max_length=150)
    faculty = models.CharField(max_length=150)
    major = models.CharField(max_length=200)
    start_date = models.DateField(auto_now_add=False)
    still_studying = models.BooleanField(default=False)
    end_date = models.DateField(auto_now_add=False, null=True)

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
    icon = models.ImageField(upload_to='images')

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
    knowledge_on = models.TextField                     # What I can do using the language

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.language


class WorkExperience(models.Model):
    """
    A model for handling what work experience I have.
    """

    types = [
        ('Remote full-time', 'Remote full-time'),
        ('Remote part-time', 'Remote part-time'),
        ('Remote contract', 'Remote contract'),
        ('In-person full-time', 'In-person full-time'),
        ('In-person part-time', 'In-person part-time'),
        ('In-person contract', 'In-person contract'),
        ('Freelance', 'Freelance'),
    ]

    work_place = models.CharField(max_length=150)
    as_a = models.CharField(max_length=150)         # EXAMPLE: Full-stack Web Developer
    employment_type = models.CharField(max_length=100, choices=types)
    started = models.DateField(auto_now_add=False)  # The date I started working at the specified work place
    still_working = models.BooleanField(default=False)
    ended = models.DateField(auto_now_add=False)    # The date I ended working at the specified work place
    comment = models.TextField()

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.work_place
