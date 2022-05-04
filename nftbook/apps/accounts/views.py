from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.views import View
from django.views.generic import TemplateView


class SignUpView(View):
    template_name = "accounts/signup.html"

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("accounts:dashboard")
        else:
            context = {
                "form": form
            }
        return render(request, self.template_name, context)


class DashboardView(TemplateView):
    template_name = "accounts/dashboard/index.html"
