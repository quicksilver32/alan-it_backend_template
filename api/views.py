from django.http import JsonResponse
from rest_framework.views import APIView


class GetData(APIView):

    def get(self, request):
        # Ваш код для обработки данных
        return JsonResponse({"response": "ok"})
