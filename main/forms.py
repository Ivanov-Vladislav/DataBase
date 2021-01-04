from .models import Human, Task1
from django.forms import ModelForm, TextInput, Textarea

class Task1Form(ModelForm):
    class Meta:
        model = Task1
        fields = ["title", "description", "id_status"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "id_status": Textarea(attrs={
                 'class': 'form-control',
                 'placeholder': 'Статус'
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

