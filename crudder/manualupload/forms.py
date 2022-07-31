# from unittest.util import _MAX_LENGTH
# from django import forms
# from django.core import validators
# from django.core.validators import RegexValidator

# # def check_for_z(value):
# #     if value[0].lower() != 'z':
# #         raise forms.ValidationError("NAME NEEDS TO START WITH Z")


# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     verifyemail = forms.EmailField(label='Enter your email again')
#     botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
#                                  validators.MaxLengthValidator(0)])
#     rollno = forms.IntegerField()
#     grade = forms.IntegerField()
#     division = forms.CharField()
#     mobno = forms.CharField(max_length=12, label="Contact Number")

#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         vmail = all_clean_data['verifyemail']
#         if email != vmail:
#             raise forms.ValidationError("Emails do not match")


# import form class from django
from django import forms
# import GeeksModel from models.py
from .models import Student
# create a ModelForm


class FormName(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.TextInput(attrs={'class': "form-control"}),
            'rollno': forms.TextInput(attrs={'class': "form-control"}),
            'grade': forms.TextInput(attrs={'class': "form-control"}),
            'division': forms.TextInput(attrs={'class': "form-control"}),
            'mobno': forms.TextInput(attrs={'class': "form-control"})
        }
