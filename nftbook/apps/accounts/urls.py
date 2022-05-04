from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

app_name = "accounts"
urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path("register/", views.SignUpView.as_view(), name="signup"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard")
]
