from .models import Human, Task1, status, branch
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
        fields = ["first_name", "second_name", "id_branch"]
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "second_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "id_branch": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Отдел разработки'
            }),
        }

class branchform(ModelForm):
    class Meta:
        model = branch
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
        }
