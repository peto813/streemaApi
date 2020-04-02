import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.templatetags.static import static
from django.conf import settings

# Create your views here.
class RelatedStationsView(APIView):
    permission_classes= (AllowAny,)
    def get(self, request):
        with open(settings.STATIC_ROOT+'/related_stations.json', 'r') as f:
            distros_dict = json.load(f)
        return Response(distros_dict, status=status.HTTP_200_OK)