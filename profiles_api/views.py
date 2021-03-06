from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permssions

class HelloApiView(APIView):
    """Test APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of api view features"""

        an_APIView = ['Uses HTTTP method as functions(GET, POST, PUT, PATCH, DELETE)',
                      'Is similar to the traditional django view',
                      'Gives you most control over your logic',
                      'Is mapped manually to URLs']

        return Response({'message': 'Hello World !', 'an_APIView': an_APIView})

    def post(self, request):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle Updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Hamndele a partial update an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test Viewset API"""

    def list(self, request):
        """Get hello message"""
        a_viewset = ['Uses actions (list, create, retrieve, update, partial_update)',
                     'Automatically maps to URLs using Routers',
                     'Provides more functionality with less code']
        return Response({'message': 'Hello !!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handling gating an object by this ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'http_method': 'DELETE'})
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permssions.UpdateOwnProfile, )