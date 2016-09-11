from rest_framework import serializers

from django.contrib.auth.models import User

from models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user')

    class Meta:
        model = Activity
        fields = ('id', 'user', 'name', 'description', 'start_datetime', 'end_datetime')



class UserSerializer(serializers.ModelSerializer):
    activities = serializers.PrimaryKeyRelatedField(many=True, queryset=Activity.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'activities')