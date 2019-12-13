
class TranscriptionConstants:
    """
    Constants related to model Transcription
    """
    NAME_MAX_LENGTH   = 50
    STATUS_MAX_LENGTH = 15


class TranscriptionStatus:
    """
    Status for model Transcription.
    """
    CONVERTING = "converting"
    CONVERTED  = "converted"
    FAILED     = "failed"

    CHOICES = [
        (CONVERTING, "Converting"),
        (CONVERTED, "Converted"),
        (FAILED, "Failed")
    ]
