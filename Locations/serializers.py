from rest_framework import serializers
from .models import Locations
from Compaies.models import Compaies
from Devices.models import Devices


class LocationSerialaizer(serializers.Serializer):
    latitude = serializers.DecimalField(max_digits=9, decimal_places=5)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=5)
    created_at = serializers.DateField()
    company_id = serializers.PrimaryKeyRelatedField(queryset=Compaies.objects.all())
    device_id = serializers.PrimaryKeyRelatedField(queryset=Devices.objects.all())
    data = serializers.JSONField()

    def create(self, validated_data):
        return Locations.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.company_id = validated_data.get('company_id', instance.company_id)
        instance.device_id = validated_data.get('device_id', instance.device_id)
        instance.data = validated_data.get('data', instance.data)

        instance.save()
        return instance
