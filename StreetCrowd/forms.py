from django import forms


class dataUploadForm(forms.Form):
    my_file = forms.FileField()
