# encoding: utf-8

from django import forms

from crispy_forms.layout import Layout, Fieldset

from core.helpers import horizontal_form_helper

from .models import SignupExtra

class SignupExtraForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignupExtraForm, self).__init__(*args, **kwargs)
        self.helper = horizontal_form_helper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(u'Lisätiedot',
                'shirt_size'
            )
        )


    class Meta:
        model = SignupExtra
        exclude = ('signup')