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

# Index Boards - Signed in users can view all the boards created
# Create boards - with ownership
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

# Show single board - no ownership required. any signed in user can view the board detail
# Delete board - ownership required.
class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
      """Show request"""
      board = get_object_or_404(Board, pk=pk)
      # if not request.user.id == board.owner.id:
      #     raise PermissionDenied('Unauthorized, you do not own this board')
      data = BoardSerializer(board).data
      return Response({ 'board': data })

    def delete(self, request, pk):
      """Delete request"""
      board = get_object_or_404(Board, pk=pk)
      if not request.user.id == board.owner.id:
          raise PermissionDenied('Unauthorized, you do not own this board')
      board.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
