from django.shortcuts import render
from django.views.generic import TemplateView, View
# A mixin for users who have logged in, which checks the login requirement
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .forms import SignInForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages

class Home(LoginRequiredMixin, TemplateView):
    login_url = 'signin'
    template_name = "accounts/home.html"


class Signin(View):
    def get(self, *args, **kwargs):
        form = SignInForm()
        context = {
            "form": form
        }
        return render(self.request, "accounts/signIn.html", context)
    def post(self, request):
        form = SignInForm(request.POST)
        
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "Invalid username or password")
                # return redirect('signup')
        return render(request, "accounts/signIn.html", {"form": form})

class Signup(TemplateView):
    template_name = "accounts/signup.html"

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('signin')
