from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import AccessToken
from accounts.models import CustomUser

class IsVerifiedView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        try:
            user_data = AccessToken(kwargs.get("token"))
            user_id = user_data["user_id"]
            user = get_object_or_404(CustomUser, id=user_id)
            user.is_verified = True
            user.save()
            return Response({"detail": "your account verified successfully"})
        except:
            return Response(
                {
                    "detail": "your token may be expired or changed structure...",
                    "resend email": "http://127.0.0.1:8080/accounts/api/V1/resend",
                }
            )