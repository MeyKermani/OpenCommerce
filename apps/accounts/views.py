from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login

from apps.accounts.forms import SignUpForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    pass

class SignupView(FormView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)



