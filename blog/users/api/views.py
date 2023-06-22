# la vista del end point para que el usuario se pueda registrar
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
#from users.models import User
from users.api.serializers import UserRegisterSerializer

class RegisterView(APIView):
    def post(self, request):
        #print('Registrando un usuario')
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        #return Response(status=status.HTTP_200_OK, data='todo ok')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
