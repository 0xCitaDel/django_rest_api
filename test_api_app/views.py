from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import TestModel

class Simple(APIView):

    def post(self, request):
        new_test_data = TestModel.objects.create(
            name = request.data['name'],
            description = request.data['description'],
            phone_number = request.data['phone_number'],
            is_alive = request.data['is_alive'],
            amount = request.data['amount']
        )
        return JsonResponse({"data": model_to_dict(new_test_data)})
    
    def get(self, request):
        content = TestModel.objects.all().values()
        return JsonResponse({"content": list(content)})
