from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('dashboard')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Save user
        self.object = form.save()
        # Auto login
        login(self.request, self.object)
        return redirect(self.get_success_url())