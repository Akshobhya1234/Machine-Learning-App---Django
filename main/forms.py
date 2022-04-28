from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import searchUser, userDetails, modelResult

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class Search1(forms.ModelForm):

    class Meta:
        model = searchUser

        fields = ['FileName','UploadCSV','label','UserName']

class selectChoiceForm(forms.ModelForm):
    class Meta:
        model = userDetails
        fields = ['model','userName']

class modelResultForm(forms.ModelForm):
    class Meta:
        model=modelResult
        fields='__all__'

