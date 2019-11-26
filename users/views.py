from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import AuthForm, RegisterForm, EditProfileForm


class DiplomaLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('jobs:tree')
    authentication_form = AuthForm


class DiplomaLogoutView(LogoutView):
    next_page = 'users:login'


class UserRegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'


class EditProfileView(LoginRequiredMixin, UpdateView):
    form_class = EditProfileForm
    template_name = 'users/edit-profile.html'
    success_url = reverse_lazy('users:edit-profile')

    def get_object(self, queryset=None):
        return self.request.user
