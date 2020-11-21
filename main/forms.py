from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "time", "difficulty", "num_people", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "time": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Продолжительность'
            }),
            "difficulty": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сложность работы'
            }),
            "num_people": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество людей'
            }),
            "task": Textarea(attrs={
                 'class': 'form-control',
                 'placeholder': 'Введите описание'
            }),
        }


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].widget.attrs = {'class': 'form-control form-control-sm'}




