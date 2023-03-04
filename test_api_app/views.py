from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import TestModelSerializer
from .models import TestModel

class Simple(APIView):

    def post(self, request):
        serializer = TestModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_test_data = TestModel.objects.create(
            name = request.data['name'],
            description = request.data['description'],
            phone_number = request.data['phone_number'],
            is_alive = request.data['is_alive'],
            amount = request.data['amount']
        )
        return JsonResponse({"data": TestModelSerializer(new_test_data).data})
    
    def get(self, request):
        content = TestModel.objects.all()
        return JsonResponse({"content": TestModelSerializer(content, many=True).data})
