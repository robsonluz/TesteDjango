
from rest_framework import routers, serializers, viewsets, mixins
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
        fields = ['id', 'titulo', 'sinopse', 'atores']

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

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'duvidas', DuvidaViewSet)
router.register(r'filmes', FilmeViewSet)
router.register(r'cidades', CidadeViewSet)
router.register(r'usuarios-create', CreateUsuarioViewSet)
