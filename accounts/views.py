from django.http import HttpRequest, HttpResponse
from .forms import SignUpForm, LoginForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView


class SignUpView(generic.CreateView):
    """Представление для регистрации нового пользователя."""

    form_class = SignUpForm
    success_url = reverse_lazy("login")
    initial = None
    template_name = "registration/signup.html"

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Обрабатывает входящий запрос до вызова основного метода.
        Если пользователь уже аутентифицирован, перенаправляет его на страницу
        списка постов. В противном случае продолжает обработку запроса."""

        if request.user.is_authenticated:
            return redirect("blog:post_list")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Обрабатывает GET-запрос. Возвращает форму регистрации."""

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Обрабатывает POST-запрос. Создает нового пользователя."""

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Учетная запись, созданная для {username}")
            return redirect("login")
        return render(request, self.template_name, {"form": form})


class CustomLoginView(LoginView):
    """Кастомное представление для входа пользователя в систему."""

    form_class = LoginForm

    def form_valid(self, form: LoginForm) -> HttpResponse:
        """Выполняется при успешной валидации формы входа.
        Проверяет, была ли установлена опция «Запомнить меня». Если опция отключена,
        устанавливает срок хранения сессии равным 0 (сессия закроется при закрытии браузера).
        """

        remember_me = form.cleaned_data.get("remember_me")

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super().form_valid(form)
