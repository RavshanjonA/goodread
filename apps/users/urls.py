from django.urls import path

from apps.users.views import UserLoginView, UserRegisterView

app_name = "users"
urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login-page"),
    path('register/', UserRegisterView.as_view(), name="register-page")
]
