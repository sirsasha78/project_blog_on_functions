from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        label="Имя",
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1", "placeholder": "Введите имя"}
        ),
    )
    last_name = forms.CharField(
        max_length=100,
        label="Фамилия",
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1", "placeholder": "Введите фамилию"}
        ),
    )
    username = forms.CharField(
        max_length=30,
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "Введите имя пользователя",
            }
        ),
    )
    email = forms.EmailField(
        max_length=200,
        label="Электронная почта",
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "Введите вашу электронную почту",
            }
        ),
    )
    password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-1", "placeholder": "Введите пароль"}
        ),
        label="Пароль",
    )
    password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-1", "placeholder": "Повторите пароль"}
        ),
        label="Повтор пароля",
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1", "placeholder": "Имя пользователя"}
        ),
        label="Имя пользователя",
    )
    password = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-1", "placeholder": "Пароль"}
        ),
        label="Пароль",
    )
    remember_me = forms.BooleanField(required=False, label="Запомнить меня")

    class Meta:
        model = User
        fields = ["username", "password", "remember_me"]


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1", "placeholder": "Имя пользователя"}
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1", "placeholder": "Электронная почта"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email"]


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control mb-1"})
    )
    bio = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Profile
        fields = ["avatar", "bio"]
