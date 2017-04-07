# -*- coding: utf-8 -*-
from django import forms

from pydaygal.schedules.models import Presentation


class PresentationForm(forms.ModelForm):

    class Meta:
        model = Presentation
        fields = ["keynote", "keynote_url"]
