from django.forms import ModelForm
from django import forms
from shortener import models
#from formValidationApp.models import *

class In_Form(forms.Form):
    url_input = forms.URLField( )

    #class Meta:
    #    # write the name of models for which the form is made
    #    model = models.URL
#
#        # Custom fields
#        fields =["username", "gender", "text"]



    def clean(self):

        # data from the form is fetched using super function
        super(In_Form, self).clean()

        # extract the username and text field from the data
        #username = self.cleaned_data.get('username')
        text = self.cleaned_data.get('url_input')

        # conditions to be met for the username length
        #if len(username) < 5:
        #    self._errors['username'] = self.error_class([
        #        'Minimum 5 characters required'])
        if len(text) <8:
            self._errors['url_input'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])

        # return any errors if found
        return self.cleaned_data
