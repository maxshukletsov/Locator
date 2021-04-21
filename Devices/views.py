from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Devices
from .serializers import DevicesSerialaizer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class DeviceView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        devices = Devices.objects.all()
        context = {
            "devices": devices.values(),
        }
        return Response(context)

    def post(self, request):
        devices = request.data.get('devices')
        serializer = DevicesSerialaizer(data=devices, many=True)
        if serializer.is_valid(raise_exception=True):
            devices_saved = serializer.save()
        return Response({"success": "Devices '{}' created successfully".format(devices_saved)})

    def put(self, request):
        data = request.data.get('devices')
        print(data)
        pk = data[0]['id']
        saved_devices = get_object_or_404(Devices.objects.all(), pk=pk)
        serializer = DevicesSerialaizer(instance=saved_devices, data=data[0], partial=True)
        if serializer.is_valid(raise_exception=True):
            devices_saved = serializer.save()
        return Response({
            "success": "Device '{}' updated successfully".format(devices_saved)
        })
