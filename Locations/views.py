from django.shortcuts import render, redirect
import folium
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Locations
from .serializers import LocationSerialaizer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# API Locations
class MapView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        locations = Locations.objects.all()
        context = {
            "locations": locations.values(),
        }
        return Response(context)

    def post(self, request):
        locations = request.data.get('locations')
        serializer = LocationSerialaizer(data=locations, many=True)
        if serializer.is_valid(raise_exception=True):
            locations_saved = serializer.save()
        return Response({"success": "Location '{}' created successfully".format(locations_saved)})

    def put(self, request):
        data = request.data.get('locations')
        pk = data[0]['id']
        saved_locations = get_object_or_404(Locations.objects.all(), pk=pk)
        serializer = LocationSerialaizer(instance=saved_locations, data=data[0], partial=True)
        if serializer.is_valid(raise_exception=True):
            locations_saved = serializer.save()
        return Response({
            "success": "Location '{}' updated successfully".format(locations_saved)
        })


def locator(request):
    data = Locations.objects.values_list('id', 'latitude', 'longitude')
    m = folium.Map(location=[25.0, 25.0], zoom_start=5, width='50%', height='60%')
    for markers in data:
        folium.Marker(location=[markers[1], markers[2]], tooltip=f'{markers[0]}',).add_to(m)
    context = {'map': m._repr_html_()}
    return render(request, 'map.html', context)


# переадресовываем с / на /map/
def redirect_view(request):
    request = redirect('/map/')
    return request