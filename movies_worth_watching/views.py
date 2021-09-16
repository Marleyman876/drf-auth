from django.shortcuts import render
from rest_framework import generics
from .serializers import Movies_Worth_WatchingSerialiers
from .models import Movies_Worth_Watching
from .permissions import IsOwnerOrReadOnly

class Movies_Worth_WatchingList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Movies_Worth_Watching.objects.all()
  serializer_class = Movies_Worth_WatchingSerialiers

class Movies_Worth_WatchingDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Movies_Worth_Watching.objects.all()
  serializer_class = Movies_Worth_WatchingSerialiers