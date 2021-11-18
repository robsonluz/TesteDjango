
from rest_framework import routers, serializers, viewsets, mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework.permissions import IsAuthenticated

#from django.contrib.auth import authenticate, user_logged_in
from django.contrib.auth import authenticate, login, logout
from todo.models import Duvida, Filme, Ator, Usuario, Cidade

# Serializers define the API representation.
class DuvidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duvida
        fields = ['pergunta', 'resposta']

# ViewSets define the view behavior.
class DuvidaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Duvida.objects.all()
    serializer_class = DuvidaSerializer


# Serializers define the API representation.
class AtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ator
        fields = ['id', 'nome']

# Serializers define the API representation.
class FilmeSerializer(serializers.ModelSerializer):
    atores = AtorSerializer(many=True, read_only=True)
    class Meta:
        model = Filme
        fields = ['id', 'titulo', 'sinopse', 'atores', 'fotoCapa']

# ViewSets define the view behavior.
class FilmeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer        


# Serializers define the API representation.
class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ['id', 'nome']

# ViewSets define the view behavior.
class CidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cidade.objects.all().order_by('nome')
    serializer_class = CidadeSerializer  


#Cadastro
class CreateUsuarioSerializer(serializers.ModelSerializer):
    cidade: CidadeSerializer()
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'telefone', 'senha', 'cidade']

class CreateUsuarioViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  serializer_class = CreateUsuarioSerializer   
  queryset = Usuario.objects.all()



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'password',
        ]

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance

class UserRegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  serializer_class = UserRegistrationSerializer  


class LoginViewSet(ViewSet):
  @staticmethod
  def create(request: Request) -> Response:
      user = authenticate(
          username=request.data.get('username'),
          password=request.data.get('password'))

      if user is not None:
        login(request, user)
        return JsonResponse({"detail": "Success"})
      else:
        return JsonResponse(
            {"detail": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class UserDetailsViewSet(ViewSet):
  serializer_class = UserDetailsSerializer
  permission_classes = [IsAuthenticated]
  @staticmethod
  def list(request: Request) -> Response:
    content = {'not_done': 1}
    print(request.user)
    print(content)
    serializer = UserDetailsSerializer(request.user, many=False)
    #return 
    return Response(serializer.data)


class LogoutViewSet(ViewSet):
  permission_classes = [IsAuthenticated]
  @staticmethod
  def list(request: Request) -> Response:
    logout(request)
    content = {'logout': 1}
    return Response(content)    



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'duvidas', DuvidaViewSet)
router.register(r'filmes', FilmeViewSet)
router.register(r'cidades', CidadeViewSet)
router.register(r'usuarios-create', CreateUsuarioViewSet)
router.register(r'currentuser', UserDetailsViewSet, basename="Currentuser")
router.register(r'login', LoginViewSet, basename="Login")
router.register(r'logout', LogoutViewSet, basename="Logout")
router.register(r'user-registration', UserRegistrationViewSet, basename="User")
