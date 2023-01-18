"""Defines models for Foreign Key relationships."""
from django.db import models


class Media(models.Model):
    """"
    A model for handling the type of social media.
    """

    class Meta:

        verbose_name = 'Media'
        verbose_name_plural = 'Media'
    
    media_type = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='media/images')

    objects = models.Manager()

    def __str__(self) -> str:
        
        return self.media_type
