from rest_framework import serializers
from .models import Devices
from Compaies.models import Compaies


class DevicesSerialaizer(serializers.Serializer):
    company_id = serializers.PrimaryKeyRelatedField(queryset=Compaies.objects.all())
    device_id = serializers.CharField(max_length=255)
    device_model = serializers.CharField(max_length=255)
    created_at = serializers.DateField()
    app = serializers.CharField(max_length=255)
    version = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Devices.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.company_id = validated_data.get('company_id', instance.company_id)
        instance.device_id = validated_data.get('device_id', instance.device_id)
        instance.device_model = validated_data.get('device_model', instance.device_model)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.app = validated_data.get('app', instance.app)
        instance.version = validated_data.get('version', instance.version)
        instance.save()
        return instance
