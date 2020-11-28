from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "date", "id_person", "id_status"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
            "id_person": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Создатель'
            }),
            "id_status": Textarea(attrs={
                 'class': 'form-control',
                 'placeholder': 'Статус'
            }),
        }


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].widget.attrs = {'class': 'form-control form-control-sm'}




