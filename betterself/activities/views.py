from django.contrib.auth.models import User
from rest_framework import generics, permissions

import serializers
from permissions import IsOwnerOrReadOnly
from models import Activity


class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = serializers.ActivitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = serializers.ActivitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer