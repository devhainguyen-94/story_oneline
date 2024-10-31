from django import forms
from main.models import Audio

class AudioUploadForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['audio_file']