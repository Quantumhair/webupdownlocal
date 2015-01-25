from django import forms

from .models import Rssrecord

class RssRecordsForm(forms.ModelForm):
    class Meta:
        model = Rssrecord
        fields = ( 'url',
        )
        widgets = {
            'url': forms.Textarea(
                attrs={
                    'placeholder':'Enter entire URL (including http:// or https://',
                    'class':'form-control'
                }
            ),
        }
class CsvUploadForm(forms.Form):
    csvFile = forms.FileField(label='Select Your File For Upload')