from rest_framework import serializers

class TestModelSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    phone_number = serializers.IntegerField()
    is_alive = serializers.BooleanField()
    amount = serializers.FloatField()
    extra_name = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)