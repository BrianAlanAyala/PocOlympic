
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class BienvenidoView(APIView):
    def get(self, request):
        nombre = request.GET.get('nombre', 'Desconocido')
        return Response({"mensaje": f"Hola {nombre}, bienvenido a Hola Mundo!"}, status=status.HTTP_200_OK)

