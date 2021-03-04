from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test APIView"""
    serializer_class = serializers.HelloSerialzer

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

    def delete(self, request , pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
