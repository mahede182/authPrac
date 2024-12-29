from django.shortcuts import render
from django.views.generic import TemplateView, View
# A mixin for users who have logged in, which checks the login requirement
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Home(LoginRequiredMixin, TemplateView):
    login_url = 'signin'
    template_name = "accounts/home.html"


class Signin(View):
    def get(self, *args, **kwargs):
        return render(self.request, "accounts/signIn.html")
    def post(self, request):
        pass

class Signup(TemplateView):
    template_name = "accounts/signup.html"
