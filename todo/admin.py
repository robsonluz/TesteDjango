from django.contrib import admin

from .models import Ator
from .models import Filme
from .models import Sessao
from .models import Sala

admin.site.register(Ator)
admin.site.register(Filme)
admin.site.register(Sessao)
admin.site.register(Sala)
