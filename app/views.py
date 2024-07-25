from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import LoginFrom, SignUpForm


class IndexView(TemplateView):
    template_name = "index.html"


class SignupView(CreateView):
    form_class = SignUpForm  # 作成した登録用フォームを設定
    template_name = "app/signup.html"
    success_url = reverse_lazy("app:index")  # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "app/login.html"


class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("app:index")
