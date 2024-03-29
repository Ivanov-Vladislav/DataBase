from .models import person, Task1, status, branch, Avatar, team, team_person
from django.forms import ModelForm, TextInput

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
        model = person
        fields = ["first_name", "second_name", "avatar"]

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

class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ["avatar"]


class TeamForm(ModelForm):
    class Meta:
        model = team
        fields = ["name", "date", "description"]

class Team_Person_Form(ModelForm):
    class Meta:
        model = team_person
        fields = ["id_team"]