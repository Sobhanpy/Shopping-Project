from accounts.serializers import CustomObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class Customejwtview(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer

# class VerificationView(GenericAPIView):

#     def get(self, request, *args, **kwargs):
#         user = get_object_or_404(CustomeUser, email = "admin@hamid.com")
#         token = self.get_tokens_for_user(user)
#         message = EmailMessage('email/email.html', {'user': 'hamid', "token":token}, 'admin@hamid.com', to=["admin@hamid.com"])
#         email = SendEmailWithThreading(message)
#         email.start()
#         return Response({"detail" : "email sent for your verification...!"})


#     def get_tokens_for_user(self, user):

#         refresh = RefreshToken.for_user(user)
#         return str(refresh.access_token)
