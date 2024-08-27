import mimetypes
from typing import Any
from django.db import models
from django.core.exceptions import ValidationError

def validate_audio_file(value):
    mime_type, encoding = mimetypes.guess_type(value.name)

    if not mime_type or not mime_type.startswith('audio'):
        raise ValidationError("This file is not a valid audio file")
    
class AudioFileField(models.FileField):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs['validators'] = kwargs.get('validators', []) + [validate_audio_file]
        super().__init__(*args, **kwargs)
        