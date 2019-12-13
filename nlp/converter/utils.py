import os
from celery import shared_task
from django.conf import settings
from speech_recognition import AudioFile, Recognizer


from .models import TranscriptionStatus, Transcription


@shared_task()
def convert_audio_to_text(transcription_pk):
    """
    Take the audio path and convert it to text
    Args:
        transcription_pk: Pk of Transcription that needs to be transcribed

    Returns: Transcription of file
    """
    transcription_file = Transcription.objects.get(pk=transcription_pk)

    audio_path = transcription_file.audio.url
    audio_path = settings.BASE_DIR + audio_path

    if not os.path.exists(audio_path):
        raise Exception("Audio file doesn't exists")

    recognizer = Recognizer()
    audio_file = AudioFile(audio_path)

    with audio_file as source:
        audio = recognizer.record(source)

    text = recognizer.recognize_google(audio)
    transcription_file.text = text
    transcription_file.status = TranscriptionStatus.CONVERTED
    transcription_file.save()


