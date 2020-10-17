from django import forms


class InputForm(forms.Form):
    in_out = forms.CharField(required=True, max_length=5)
    stu_name = forms.CharField(required=True, max_length=16)
    stu_id = forms.CharField(required=True, max_length=20)
    gate = forms.CharField(required=True, max_length=12)
