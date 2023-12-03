# urls for cusine app
from django.urls import path
from . import views
from django.urls import include

APP_NAME = "cusine"
urlpatterns = [
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("signout/", views.signout, name="signout"),
    path("get_recipes/", views.get_recipes, name="get_recipes"),
    # auth api urls
    path("auth/", views.get_user_details, name="get_user_details"),
    path("create_recipe/", views.create_recipe, name="create_recipe"),
    path("edit_recipe/", views.edit_recipe, name="create_recipe"),
    # Add other paths as needed
]
