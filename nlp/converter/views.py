from django.template.response import TemplateResponse
from django.db import transaction

from .models import Transcription, TranscriptionStatus
from .utils import convert_audio_to_text


def home(request):
    """
    Home page
    Args:
        request:

    Returns:

    """
    message = {
        "class": "text-success",
        "text" : ""
    }
    if request.method == "POST":

        try:
            name  = request.POST['name']
            audio = request.FILES['audio']
            with transaction.atomic():
                transcription        = Transcription.objects.create(name=name, audio=audio)

                # Asynchronously convert the audio into text
                convert_audio_to_text(transcription.pk)
                # convert_audio_to_text.delay(transcription.pk)

            message['text'] = "File uploaded successfully"
            if not name:
                raise Exception("Please enter the name for this conversion")
            if not audio:
                raise Exception("Please select the audio file for the conversion")

        except KeyError:
            raise Exception("Either name or audio is missing from the form data")

        except Exception as error:
            message['text']  = error
            message['class'] = 'text-danger'
    transcriptions = Transcription.objects.all().only('name').order_by('-updated_at')

    ctx = {
        "transcriptions": transcriptions,
        "message"       : message
    }

    return TemplateResponse(request, 'home.html', ctx)


def delete_transcription(request, pk):
    message = {
        "class": "text-success",
        "text" : ""
    }
    try:
        transcriptions = Transcription.objects.filter(pk=pk)
        if not transcriptions.exists():
            raise Exception("Transcription which you are trying to delete doesn't exists")

        transcription = transcriptions.first()
        transcription.delete()

        message['text'] = "Transcription deleted successfully"
    except Exception as error:
        message['text']  = error
        message['class'] = 'text-danger'

    transcriptions = Transcription.objects.all().only('name').order_by('-updated_at')
    ctx = {
        "transcriptions": transcriptions,
        "message": message
    }
    return TemplateResponse(request, 'home.html', ctx)
