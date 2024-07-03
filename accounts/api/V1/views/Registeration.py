from rest_framework.generics import GenericAPIView
from accounts.api.V1.serializers import RegisterationSerializer
from accounts.models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .tasks import send_email_with_celery


class RegistrationView(GenericAPIView):
    """
    this class is for create user
    """

    serializer_class = RegisterationSerializer

    def post(self, request, *args, **kwargs):

        serializer = RegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_object_or_404(
                CustomUser, email=serializer.validated_data["email"]
            )
            token = self.get_tokens_for_user(user)
            send_email_with_celery.delay("email/email.html", token, "admin@hamid.com", [user.email])
            
            
            

            return Response({"detail": "if email is on our database email sent for your verification...!"})

            # print (serializer.validated_data)
            # data = {
            #     'email': serializer.validated_data['email']
            # }
            # return Response(data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)