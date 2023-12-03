from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.authentication import TokenAuthentication


@api_view(["POST"])
@permission_classes([AllowAny])
def signin(request):
    username = request.data.get("username")
    password = request.data.get("password")
    print(username, password)
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        # get user
        token, _ = Token.objects.get_or_create(user=user)

        # convert user to json
        user = {
            "username": user.username,
            "email": user.email,
        }

        return Response({"token": token.key, "user": user}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    user = User.objects.create_user(username, email, password)
    user.save()

    return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
def signout(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def get_recipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "OPTIONS"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def get_user_details(request):
    token = request.headers.get("auth-token").split(" ")[0]
    print(token)
    user = Token.objects.get(key=token).user

    user_details = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        # Add other user details as needed
    }
    return Response(user_details)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def create_recipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors)
