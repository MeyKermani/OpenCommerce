from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import login


from apps.accounts.forms import SignUpForm, ProfileUpdateForm, UserUpdateForm
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
    
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

class ProfileUpdateView(LoginRequiredMixin, View):
    template_name = 'accounts/profile_edit.html'

    def get(self, request, *args, **kwargs):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect ('accounts:profile')

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, self.template_name, context)