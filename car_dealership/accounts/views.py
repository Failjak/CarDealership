from rest_framework.permissions import AllowAny
from rest_framework import generics, status

from accounts.serializers import UserSerializer
from rest_framework.response import Response


class CreateUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            {
                'message': 'User has been created successful!',
                'user': serializer.data
             },
            status=status.HTTP_201_CREATED,
            headers=headers
        )
