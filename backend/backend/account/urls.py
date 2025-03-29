from django.urls import path

from .views import LoginView, TokenRefreshView, HomeView

urlpatterns = [
    path('token/refresh', TokenRefreshView.as_view()),
    path('login', LoginView.as_view()),
    path('home', HomeView.as_view())
]