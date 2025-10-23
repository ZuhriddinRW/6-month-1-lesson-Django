import re

from django import forms
from django.core.exceptions import ValidationError
from django_app.models import *


class NewsForm ( forms.ModelForm ) :
    class Meta :
        model = News
        fields = '__all__'
        widgets = {
            'content' : forms.Textarea ( attrs={
                'class' : 'form-control rounded-3 border-primary',
                'rows' : 6,
                'style' : 'resize: vertical; min-height: 120px;'
            } ),

            'title' : forms.TextInput ( attrs={
                'class' : 'form-control rounded-3 border-primary mb-0',
            } ),

            'category' : forms.Select ( attrs={
                'class' : 'form-select rounded-3 border-primary',
            } )
        }

    def clean_title(self) :
        title = self.cleaned_data['title']

        if re.match ( r'\d', title ) :
            print ( '======================== Hello World! ========================' )
            raise ValidationError ( 'Title must not to contain digits' )
        return title