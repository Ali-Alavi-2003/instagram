from rest_framework import serializers
from accounts.services.otp import OtpService
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model



User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'phone_number',
        )

class SendOtpSerializer(serializers.Serializer):
    phone = serializers.RegexField(
        regex=r"^09\d{9}$",
        max_length=11,
        error_messages={
            "invalid": "شماره موبایل معتبر نیست"
        }
    )

    def create(self, validated_data):
        phone = validated_data['phone']
        otp = OtpService.generate_otp()
        OtpService.set_otp(phone, otp)

        print(f'Phone: {phone}')
        print(f'Code: {otp}')
        return validated_data
    

class VerifyOtpSerializer(serializers.Serializer):
    phone = serializers.RegexField(
        regex=r"^09\d{9}$",
        max_length=11,
        error_messages={
            "invalid": "شماره موبایل معتبر نیست"
        }
    )
    otp = serializers.CharField(max_length = 6)


    def validate(self, attrs):
        identifier = attrs.get('phone_number') or attrs.get('phone') 
        otp_code = attrs.get('otp')
        user, created = User.objects.get_or_create(
            phone_number=identifier,
            defaults={
                'is_active': True,
            }
        )

        attrs['user'] = user
        return attrs

    

    def create(self, validated_data):
        user = validated_data['user']
        refresh = RefreshToken.for_user(user)

        return {
            'Access': str(refresh.access_token),
            'Refresh': str(refresh)
        }