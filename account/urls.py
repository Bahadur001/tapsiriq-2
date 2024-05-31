

from django.urls import path
from .views import register_view, login_view, logout_view, contact_view
app_name = "account"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("contact/", contact_view, name="contact"),
]
