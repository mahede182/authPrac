from django.contrib import admin
from django.urls import path, include
from accounts.views import Home, Signin, Signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("signin/", Signin.as_view(), name="signin"),
    path("signup/", Signup.as_view(), name="signup")
]
