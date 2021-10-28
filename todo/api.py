
from rest_framework import routers, serializers, viewsets
from todo.models import Duvida, Filme, Ator

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
class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer        

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'duvidas', DuvidaViewSet)
router.register(r'filmes', FilmeViewSet)
