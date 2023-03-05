from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TestModelSerializer
from .models import TestModel

class Simple(APIView):

    def post(self, request):
        serializer = TestModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data})
    
    def get(self, request):
        content = TestModel.objects.all()
        return Response({"content": TestModelSerializer(content, many=True).data})
    
    def put(self, request, *args, **kwargs):
        model_id = kwargs.get('id', None)
        if not model_id:
            return Response({'error': 'method / PUT / not allowed'})
        try:
            isinstance = TestModel.objects.get(id=model_id)
        except:
            return Response({'error': 'Object does not exist'})
        serializer = TestModelSerializer(data=request.data, instance=isinstance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data})
