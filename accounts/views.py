from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserCreateForm


class SignUpView(CreateView):
    
    
    # def get(self, request):
  form_class = UserCreateForm
  success_url = reverse_lazy('login')
  
  template_name = 'registration/signup.html'
        # return render(request, template_name, {
        #   'form': form_class
        # })

class Sayhi(CreateView):
  def get(self, request):
      return render(request, "accounts/sign_up.html", {"test":"test"})
