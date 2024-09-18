from django.contrib import admin
from .models import Template
from .models import Empresa
from .models import administrador
from .models import Foto
from .models import Sitio
from .models import Tecnico
from .models import relatorio_final


admin.site.register(Template)
admin.site.register(Empresa)
admin.site.register(administrador)
admin.site.register(Foto)
admin.site.register(Sitio)
admin.site.register(Tecnico)
admin.site.register(relatorio_final)

