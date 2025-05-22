from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LoginSerializer

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data
            user = authenticate(username=validated_data['username'], password=validated_data['password'])
            if user:
                token = user.get_token()
                return Response(data=token, status=status.HTTP_200_OK)
            return Response(data={"message": _("User not found")}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(data={"error": f"Internal Server Error-{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

