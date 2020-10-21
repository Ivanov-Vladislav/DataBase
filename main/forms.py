from .models import Task, Human
from django.forms import ModelForm, TextInput, Textarea

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

class HumanForm(ModelForm):
    class Meta:
        model = Human
        fields = ["Surname", "Forename", "age", "evulation_work"]
        widgets = {
            "Surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "Forename": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "age": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            "evulation_work": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оценка работы'
            }),
        }
