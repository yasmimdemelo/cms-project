from django.forms import ModelForm
from .models import Documents

class DocumentsForm(ModelForm):
    class Meta:
        model = Documents
        fields = ['title', 'descricao']
