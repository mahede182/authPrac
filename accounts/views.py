# Django core imports
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# A mixin for users who have logged in, which checks the login requirement
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView, View

# Local imports
from .forms import SignInForm, SignUpForm
from .mixins import LogoutRequiredMixin

@method_decorator(never_cache, name='dispatch')
class Home(LoginRequiredMixin, TemplateView):
    login_url = 'signin'
    template_name = "accounts/home.html"

@method_decorator(never_cache, name='dispatch')
class Signin(LogoutRequiredMixin, View):
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

@method_decorator(never_cache, name='dispatch')
class Signup(LogoutRequiredMixin, TemplateView):
    template_name = "accounts/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect(self.success_url)
        else:
            # Check if the error is due to password mismatch
            if 'Passwords do not match' in str(form.errors.get('__all__', '')):
                messages.error(request, "Passwords do not match. Please try again.")
        return render(request, self.template_name, {'form': form})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('signin')
