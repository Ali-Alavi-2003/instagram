from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView

from accounts.services.otp import OtpService
from accounts.serializer.authuser import (
    SendOtpSerializer,
    VerifyOtpSerializer,
)

User = get_user_model()

class SendOtpAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SendOtpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "OTP sent"}, status=status.HTTP_200_OK)
    

# class SendOtpAPIView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request: Request):
#         serializer = SendOtpSerializer(data= request.data)
#         serializer.is_valid(raise_exception= True)

#         serializer.save()

#         return Response({'message': 'OTP Sent'})


class VerifyOtpAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = VerifyOtpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.save()
        return Response(tokens, status=status.HTTP_200_OK)
    
# class VerifyOtpAPIView(APIView):
#     permission_classes =[AllowAny]
#     def post(self, request:Request):

#         serializer = VerifyOtpSerializer(data= request.data)
#         serializer.is_valid(raise_exception= True)
#         tokens = serializer.save()

#         return Response(tokens, status= status.HTTP_200_OK)