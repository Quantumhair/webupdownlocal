from django import forms

from .models import Rssrecord

class RssRecordsForm(forms.ModelForm):
    class Meta:
        model = Rssrecord
        fields = ('name', 'url', 'desc',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder':'Descriptive name',
                    'class':'col-md-12 form-control'
                }
            ),
            'url': forms.Textarea(
                attrs={
                    'placeholder':'Enter entire URL (including http:// or https://',
                    'class':'form-control'
                }
            ),
            'desc': forms.TextInput(
                attrs={
                    'placeholder':'Enter a desciption if desired',
                    'class':'form-control'
                }
            ),
        }
