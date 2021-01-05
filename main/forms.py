from .models import Human, Task1, status
from django.forms import ModelForm, TextInput, Textarea

class Task1Form(ModelForm):
    class Meta:
        model = Task1
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
        }

class statusform(ModelForm):
    class Meta:
        model = status
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
        }



class HumanForm(ModelForm):
    class Meta:
        model = Human
        fields = ["Surname", "Forename", "ages", "evulation_work"]
        widgets = {
            "Surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "Forename": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "ages": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            "evulation_work": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оценка работы'
            }),
        }

