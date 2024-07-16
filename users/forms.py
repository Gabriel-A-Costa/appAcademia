from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, SetPasswordForm
from academia.models import Aparelho
from .models import Training, Profile, Anamnese, Antropometria


class RememberMeForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(
        attrs={'class': 'login__check-input'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            return username.lower()
        return username


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="", required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Primeiro Nome'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Segundo Nome'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2',]


class UpdateUserForm(UserChangeForm):

    password = None

    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Primeiro Nome'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Segundo Nome'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']


class TrainingPlanning(forms.ModelForm):

    class Meta:
        model = Training
        fields = ['type', 'aparelho', 'qnt_series',
                  'qnt_repetitions', 'tempo', 'treino', 'tipo_treino']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user and isinstance(user, User):
            self.fields['aparelho'].queryset = Aparelho.objects.filter(
                users=user)


class FormAnamnese(forms.ModelForm):
    class Meta:
        model = Anamnese
        fields = ['meta', 'pratica_atividades', 'atividades_fisicas', 'frequencia_atividades', 'fuma', 'tempo_fumante',
                  'qnt_cigarro', 'restricao', 'tipos_restricao', 'medicamento', 'tipos_medicamento', 'dores',
                  'tipos_dores', 'acidente', 'tipos_acidentes', 'dieta', 'alergia', 'tipos_alergia',
                  'controle_pressao', 'cardiaco', 'historico_cardiaco', 'idade', 'coluna']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user = user.user


class FormAntropometria(forms.ModelForm):
    class Meta:
        model = Antropometria
        fields = [
            'massa_corporal', 'estatura', 'pescoco', 'ombro', 'torax', 'cintura', 'abdome', 'quadril', 'braco_direito',
            'ante_braco_direito', 'coxa_direito', 'panturrilha_direito', 'braco_esquerda', 'ante_braco_esquerda',
            'coxa_esquerda', 'panturrilha_esquerda', 'imc', 'gordura', 'massa_corporal_2', 'metabolismo',
            'idade_corporal', 'gordura_viceral', 'avaliado'
        ]

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user = user.user


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_img']
