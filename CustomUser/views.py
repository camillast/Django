from rest_framework.generics import ListCreateAPIView
from CustomUser.models import CustomUser
from CustomUser.serializers import UserSerializer


class UserListView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()
