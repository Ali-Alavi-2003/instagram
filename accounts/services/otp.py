import random
from django.core.cache import cache

OTP_EXP = 120


class OtpService:
    @staticmethod
    def generate_otp():
        return str(random.randint(100000, 999999))
    
    @staticmethod
    def set_otp(phone, code):
        key = f'otp:{phone}'
        cache.set(key, code, OTP_EXP)
    
    @staticmethod
    def get_otp(phone):
        key = f'otp:{phone}'
        return cache.get(key)
    
    @staticmethod
    def delete_otp(phone):
        key = f'otp:{phone}'
        cache.delete(phone)