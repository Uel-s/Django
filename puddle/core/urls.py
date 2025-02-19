from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView
from . import views
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", views.index,name="index"),
    path("about/", TemplateView.as_view(template_name="core/about.html"), name="about"),
    path("contact/",views.contact,name="contact"),
    path("privacy-policy/", TemplateView.as_view(template_name="core/privacy_policy.html"), name="privacy_policy"),
    path("terms-of-use/", TemplateView.as_view(template_name="core/terms_of_use.html"), name="terms_of_use"),
    path("signup/", views.signup,name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html",authentication_form=LoginForm),name="login" )







]
