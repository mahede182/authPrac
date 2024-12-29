from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Home(TemplateView):
    template_name = "accounts/home.html"


class Signin(TemplateView):
    template_name = "accounts/signIn.html"


class Signup(TemplateView):
    template_name = "accounts/signup.html"
