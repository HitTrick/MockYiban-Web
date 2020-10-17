from django import forms

from app_v1.models import Advice


class InputForm(forms.Form):
    in_out = forms.CharField(required=True, max_length=5)
    stu_name = forms.CharField(required=True, max_length=16)
    stu_id = forms.CharField(required=True, max_length=20)
    gate = forms.CharField(required=True, max_length=12)


class AdviceForm(forms.ModelForm):
    # name = forms.CharField(required=True, max_length=40)
    # content = forms.CharField(required=True)
    # contact_info = forms.CharField(required=True, max_length=40)
    class Meta:
        model = Advice
        fields = ["name", "content", "contact_info"]
