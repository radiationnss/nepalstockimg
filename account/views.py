from django.shortcuts import redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView

class LoginView(FormView):
  form_class = LoginForm
  success_url = 'home/'
  template_name = 'account/login.html'

  def form_valid(self, form):
    request = self.request
    email = form.cleaned_data.get("email")
    password = form.cleaned_data.get("password")
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        redirect('/')
    return super().form_invalid(form)


class RegisterView(CreateView):
  form_class = RegisterForm
  template_name = 'account/register.html'
  success_url = 'login/'
