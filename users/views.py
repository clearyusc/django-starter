import stripe

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.conf import settings

from .forms import CustomUserCreationForm


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class ProfilePageView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = get_user_model()
    context_object_name = 'user_object'
    template_name = 'profile_detail.html'
    login_url = 'account_login'

    def test_func(self):
        return self.request.path.endswith(str(self.request.user.id))


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = get_user_model()
    fields = ['username','first_name','last_name','email']
    template_name = 'profile_edit.html'
    login_url = 'account_login'

    def test_func(self):
        return self.request.path.endswith(str(self.request.user.id))
    
    def get_success_url(self):
          return reverse_lazy('profile', args=(self.request.user.pk,))


class PaymentInfoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = get_user_model()
    fields = []
    template_name = 'payment_info.html'
    login_url = 'account_login'
    extra_context = {'client_secret':stripe.SetupIntent.create().client_secret}

    def test_func(self):
        return self.request.path.endswith(str(self.request.user.id))
    
    def get_success_url(self):
          return reverse_lazy('profile', args=(self.request.user.pk,))
