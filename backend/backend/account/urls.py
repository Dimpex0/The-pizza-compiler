from django.urls import path

from .views import LoginView, TokenRefreshView, RegisterView

urlpatterns = [
    path('token/refresh', TokenRefreshView.as_view()),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view())
]