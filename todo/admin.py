from django.contrib import admin

from .models import Ator
from .models import Filme
from .models import Sessao
from .models import Sala
from .models import Duvida

admin.site.register(Ator)
admin.site.register(Filme)
admin.site.register(Sessao)
admin.site.register(Sala)
admin.site.register(Duvida)
