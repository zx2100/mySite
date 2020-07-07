from .models import UserProfile
from rest_framework import serializers


class UserProfileSerializers(serializers.ModelSerializer):
    # serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())
    class Meta:
        model = UserProfile
        exclude = (
            "password",
        )
