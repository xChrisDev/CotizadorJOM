from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@api_view(["POST"])
def login(request):
    
    user = get_object_or_404(User, username=request.data.get("username"))
    
    if not user.check_password(request.data.get("password")):
        return Response({"error": "Contraseña no valida"}, status = status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance = user)
    
    if serializer.data.get("status") == "PENDING":
        return Response({"error": "Aun no se ha aceptado tu solicitud."}, status=status.HTTP_400_BAD_REQUEST)
    
    if serializer.data.get("status") == "BANNED":
        return Response({"error": "Tu cuenta ha sido suspendida."}, status=status.HTTP_400_BAD_REQUEST)
    
    if serializer.data.get("status") == "REJECTED":
        return Response({"error": "Tu solicitud ha sido rechazada."}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)


@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        
        user = User.objects.get(username=serializer.data["username"])
        user.set_password(serializer.data["password"])
        user.save()
        
        token = Token.objects.create(user = user)
        return Response({"success": serializer.data["username"]}, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def me(request):
    return Response({"user": UserSerializer(instance=request.user).data}, status=status.HTTP_200_OK)
