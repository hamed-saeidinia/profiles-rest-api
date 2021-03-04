from rest_framework import serializers

class HelloSerialzer(serializers.Serializer):
    """Serializes a name field for APIVeiw"""
    name = serializers.CharField(max_length=10)
