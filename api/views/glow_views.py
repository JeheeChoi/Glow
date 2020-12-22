from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.glow import Glow
from ..serializers import GlowSerializer, UserSerializer

# Index Glows
# Create Glows
class Glows(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GlowSerializer
    def get(self, request):
        """Index request"""
        # Get all the glows on the board
        glows = Glow.objects.all()

        data = GlowSerializer(glows, many=True).data
        return Response({ 'glows': data })

    def post(self, request):
      """Create request"""
      # Add user to request data object 'author'
      request.data['glow']['owner'] = request.user.id
      # Serialize/ Create board
      glow = GlowSerializer(data=request.data['glow'])

      if glow.is_valid():
          glow.save()
          return Response({ 'glow': glow.data }, status=status.HTTP_201_CREATED)
      return Response(glow.errors, status=status.HTTP_400_BAD_REQUEST)
