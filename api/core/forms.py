from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'password1', 'password2', 'birth_date', 'cep', 'street', 'house_number', 'neighborhood', 'city', 'state', 
            'interests', 'services_offered', 'services_needed', 'number_of_children', 'children_age_groups'
        ]
        labels = {
            'username': 'Nome de usuária',
            'email': 'E-mail',
            'password1': 'Senha',
            'password2': 'Confirmação da Senha',
            'birth_date': 'Data de Nascimento',
            'cep': 'CEP', 
            'street': 'Rua',
            'house_number': 'Número da Casa',
            'neighborhood': 'Bairro',
            'city': 'Cidade',
            'state': 'Estado', 
            'interests': 'Interesses e Hobbies',
            'services_offered': 'Serviços Oferecidos',
            'services_needed': 'Serviços Procurados',
            'number_of_children': 'Quantos filhos você tem?',
            'children_age_groups': 'Faixa Etária dos Filhos',
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'interests': forms.Textarea(attrs={'rows': 3}),
            'services_offered': forms.Textarea(attrs={'rows': 3}),
            'services_needed': forms.Textarea(attrs={'rows': 3}),
            'children_age_groups': forms.CheckboxSelectMultiple(choices=[
                ('0-2', '0 a 2 anos'),
                ('3-5', '3 a 5 anos'),
                ('6-8', '6 a 8 anos'),
                ('9-12', '9 a 12 anos'),
            ]),
        }