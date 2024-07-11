from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    UserSerializer,
    LoginSerializer,
    InterestSerializer,
    AcceptRejectInterestSerializer,
)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Interest


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if user:
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class InterestListCreateView(generics.ListCreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    # permission_classes = [IsAuthenticated]
    print("InterestListCreateVieweeeeeee")
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
        return Response({"message": "Interest sent"}, status=status.HTTP_201_CREATED)


class InterestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    # permission_classes = [IsAuthenticated]


class AcceptInterestView(generics.UpdateAPIView):
    queryset = Interest.objects.all()
    serializer_class = AcceptRejectInterestSerializer
    # permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serialzer = self.get_serializer(instance, data=request.data)
        print("update")
        print(request.data)
        serialzer.is_valid(raise_exception=True)
        serialzer.save(accepted=True)
        print(serialzer.save(accepted=True))
        return Response({"message": "Interest accepted"}, status=status.HTTP_200_OK)


class RejectInterestView(generics.UpdateAPIView):
    queryset = Interest.objects.all()
    serialzer_class = AcceptRejectInterestSerializer
    # permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serialzer = self.get_serializer(instance, data=request.data)
        serialzer.is_valid(raise_exception=True)
        serialzer.save(accepted=False)
        return Response({"message": "Interest rejected"}, status=status.HTTP_200_OK)
