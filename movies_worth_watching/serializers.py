from rest_framework import serializers
from .models import Movies_Worth_Watching

class Movies_Worth_WatchingSerialiers(serializers.ModelSerializer):
  class Meta:
    fields = ('id','title', 'body', 'created_at')
    model = Movies_Worth_Watching