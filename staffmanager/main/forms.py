from .models import Staff
from django.forms import ModelForm, TextInput, Textarea


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ["idnumber", "email","name","number","major"]
        widgets = {
            "idnumber": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Таб.Номер'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "major": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность'
            })
        }
