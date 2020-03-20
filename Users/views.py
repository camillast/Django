from rest_framework.generics import ListCreateAPIView
from Users.models import CustomUser
from Users.serializers import UserSerializer


class UserListView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()
