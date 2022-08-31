from rest_framework.response import Response
from rest_framework.views import APIView


class Example_API(APIView):

    def get(self, request):
        msg = "GET method for the api"
        return Response(msg)
    def  post(self, request):
        
        return Response("POST method from the api")
