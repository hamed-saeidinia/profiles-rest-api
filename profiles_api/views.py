from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    def get(self, request, format=None):
        """Return a list of api view features"""
        an_APIView = ['Uses HTTTP method as functions(GET, POST, PUT, PATCH, DELETE)',
                      'Is similar to the traditional django view',
                      'Gives you most control over your logic',
                      'Is mapped manually to URLs']

        return Response({'message': 'Hello World !', 'an_APIView': an_APIView})
