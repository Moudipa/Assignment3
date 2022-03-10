from django.urls import path

from user import views


app_name = "user"

urlpatterns = [
    path("create", views.CreateUserView.as_view(), name='create'),
    path("login", views.CreateTokenView.as_view(), name="login"),
    path("me", views.ManageUserView.as_view(), name="me"),
    path("users", views.UserView.as_view(), name="users-list"),
]