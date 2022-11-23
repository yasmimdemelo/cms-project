from django.forms import ModelForm
from .models import Documents
from django import forms

class DocumentsForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Document title"}))
    descricao = forms.CharField(label='', widget=forms.Textarea(attrs={"placeholder":"Descrição"}))

    class Meta:
        model = Documents
        fields = ['title', 'descricao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label=''
        self.fields['title'].widget.attrs.update({'class': 'form-control-2'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descricao'].label=''
        self.fields['descricao'].widget.attrs.update({'class': 'form-control-2'})