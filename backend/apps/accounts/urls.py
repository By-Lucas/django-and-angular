from django.urls import path
from accounts.viewsets.viewsets import RegisterView, LoginView, UserView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]
