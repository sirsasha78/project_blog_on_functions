from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    """Форма для отправки поста по электронной почте."""

    name = forms.CharField(
        max_length=25,
        label="Имя",
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1", "placeholder": "Имя"}
        ),
    )
    email = forms.EmailField(
        label="Электронная почта",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1", "placeholder": "Электронная почта"}
        ),
    )
    to = forms.EmailField(
        label="Адрес получателя",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1", "placeholder": "Адрес получателя"}
        ),
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"class": "form-control mb-1", "placeholder": "Комментарий"}
        ),
        label="Комментарий",
    )


class CommentForm(forms.ModelForm):
    """Форма для создания и редактирования комментариев.
    Используется в представлениях для получения данных от пользователя
    при добавлении нового комментария. Основана на модели Comment."""

    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя"}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Электронная почта"}
        ),
    )
    body = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Текст"}),
    )

    class Meta:
        """Метакласс формы, определяющий связь с моделью и поля формы."""

        model = Comment
        fields = ("name", "email", "body")


class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "Введите поисковый запрос...",
            }
        ),
        label="Поиск",
    )
