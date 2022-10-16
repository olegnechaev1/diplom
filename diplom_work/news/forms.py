from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

from .models import Comment


User = get_user_model()


class AuthUserform(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User 
        fields = ('password',)
       

class RegistrUserform(forms.ModelForm):
    username = forms.CharField(help_text=False)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        
    def save(self, commit=True):
        user = super(RegistrUserform, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
