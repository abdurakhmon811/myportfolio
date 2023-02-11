from django.db import models
from .foreign_keys import Education, \
    Language, \
    Media, \
    ProgrammingLanguage, \
    WorkExperience


class About(models.Model):
    """
    A model for handling the information on me.
    """

    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'

    avatar = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
    full_bio = models.TextField()
    short_bio = models.TextField(null=True)     # Used for the main page
    programming_languages = models.ManyToManyField(ProgrammingLanguage)
    languages = models.ManyToManyField(Language)
    education = models.ManyToManyField(Education)
    work_experience = models.ManyToManyField(WorkExperience)
    skills = models.CharField(max_length=100, null=True)    # Either work related or non-releated
    hobbies = models.CharField(max_length=100, null=True)
    resume_link = models.URLField(null=True)    # Link for file located in Google Drive should be given

    objects = models.Manager()

    def __str__(self) -> str:

        return self.title


class ContactDetail(models.Model):
    """
    A model for handling contact details of mine.
    """
    
    media = models.ForeignKey(Media, on_delete=models.PROTECT)
    comment = models.TextField(null=True)

    objects = models.Manager()

    def __str__(self) -> str:
        
        return str(self.media)


class Project(models.Model):
    """
    A model for handling projects created by me.
    """

    developed = [
        ('My own', 'My own'),
        ('With team', 'With team'),
    ]

    project_created = models.CharField(max_length=100, choices=developed, null=True)
    project_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField(upload_to='images')
    date_finished = models.DateField(auto_now_add=False, null=True)

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.project_name
