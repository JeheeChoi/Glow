from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.board import Board
from ..serializers import BoardSerializer, UserSerializer

class Boards(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BoardSerializer
    def get(self, request):
        """Index request"""
        # Get all the boards:
        boards = Board.objects.all()
        # boards = Board.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = BoardSerializer(boards, many=True).data
        return Response({ 'boards': data })

    def post(self, request):
      """Create request"""
      # Add user to request data object
      request.data['board']['owner'] = request.user.id
      # Serialize/ Create board
      board = BoardSerializer(data=request.data['board'])

      if board.is_valid():
          board.save()
          return Response({ 'board': board.data }, status=status.HTTP_201_CREATED)
      return Response(board.errors, status=status.HTTP_400_BAD_REQUEST)
