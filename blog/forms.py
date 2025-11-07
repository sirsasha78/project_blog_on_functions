from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    """Форма для отправки поста по электронной почте."""

    name = forms.CharField(max_length=25, label="Имя")
    email = forms.EmailField(label="Электронная почта")
    to = forms.EmailField(label="Адрес получателя")
    comments = forms.CharField(
        required=False, widget=forms.Textarea, label="Комментарий"
    )


class CommentForm(forms.ModelForm):
    """Форма для создания и редактирования комментариев.
    Используется в представлениях для получения данных от пользователя
    при добавлении нового комментария. Основана на модели Comment."""

    class Meta:
        """Метакласс формы, определяющий связь с моделью и поля формы."""

        model = Comment
        fields = ("name", "email", "body")


class SearchForm(forms.Form):
    query = forms.CharField(label="Поиск")
