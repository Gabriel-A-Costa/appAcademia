from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Aparelho, Exercicio, Room, Treinos

class AparelhoForm(forms.ModelForm):
    class Meta:
        model = Aparelho
        fields = ['aparelho_name','aparelho_image']

        
    def __init__(self, *args, **kwargs):
        super(AparelhoForm, self).__init__(*args, **kwargs)

        self.fields['aparelho_name'].widget.attrs['class'] = 'form-control'
        self.fields['aparelho_name'].widget.attrs['placeholder'] = 'Name Apparatus'
        self.fields['aparelho_name'].label = ''
        self.fields['aparelho_name'].help_text = '<span class="form-text text-muted"><small>Obrigatório. 150 caracteres ou menos.</small></span>'

        self.fields['aparelho_image'].widget.attrs['class'] = 'form-control'
        self.fields['aparelho_image'].label = ''
        self.fields['aparelho_image'].help_text = '<span class="form-text text-muted"><small>Por favor, insira o link direto para a imagem do equipamento de academia. Certifique-se de que a URL leva diretamente à imagem para garantir a visualização correta.</small></span>'

class ExercicioForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['exercicio_type', 'exercicio_image']

    def __init__(self, *args, **kwargs):
        super(ExercicioForm, self).__init__(*args, **kwargs)

        self.fields['exercicio_type'].widget.attrs['class'] = 'form-control'
        self.fields['exercicio_type'].widget.attrs['placeholder'] = 'Exercice Type'
        self.fields['exercicio_type'].label = ''
        self.fields['exercicio_type'].help_text = '<span class="form-text text-muted"><small>Obrigatório. 150 caracteres ou menos.</small></span>'
        
        self.fields['exercicio_image'].widget.attrs['class'] = 'form-control'
        self.fields['exercicio_image'].label = ''
        self.fields['exercicio_image'].help_text = '<span class="form-text text-muted"><small>Por favor, insira um link direto para a image do exercício. Certifique-se de que a URL leva diretamente à imagem para garantir a visualização correta.</small></span>'
        

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treinos
        fields = ['treino_name','treino_image']
    
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'message']