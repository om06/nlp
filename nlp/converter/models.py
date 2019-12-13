from django.db import models

from . import TranscriptionConstants, TranscriptionStatus


class Transcription(models.Model):
    """
    Store audio and there transcription.
    """
    name   = models.CharField(max_length=TranscriptionConstants.NAME_MAX_LENGTH,
                              help_text="Name of the conversion")
    audio  = models.FileField(upload_to='audios',
                              help_text="Audio file")
    text   = models.TextField(blank=True,
                              null=True,
                              help_text="Converted text from audio file")
    status = models.CharField(max_length=TranscriptionConstants.STATUS_MAX_LENGTH,
                              choices=TranscriptionStatus.CHOICES,
                              default=TranscriptionStatus.CONVERTING,
                              help_text="Status of audio conversion")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
