import csv
from django.http import JsonResponse
from rest_framework.views import APIView


class GetData(APIView):

    def get(self, request):
        response = []
        flag = True
        with open('./short.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            for line in reader:
                if flag:
                    names = line
                    flag = False
                    continue
                else:
                    response.append({k:v for k, v in zip(names, line)})
        return JsonResponse(response, safe=False)
