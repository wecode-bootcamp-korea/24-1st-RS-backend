from django.urls import path
from users.views import LoginView, SignupView, UserDetailView, UserActivateView

urlpatterns = [
    path('/signup', SignupView.as_view()),
    path('/login', LoginView.as_view()),
    path('/detail', UserDetailView.as_view()),
    path('/avtication', UserActivateView.as_view()),
]