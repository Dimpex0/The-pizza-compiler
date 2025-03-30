from django.urls import path

from .views import LoginView, TokenRefreshView, HomeView

urlpatterns = [
    path('token/refresh', TokenRefreshView.as_view()),
    path('login', LoginView.as_view(), name="login"),
    path('home', HomeView.as_view())
]