from django.contrib import admin
from .models import TemplateRelatorio  # Corrected model name
from .models import Empresa
from .models import Administrador  # Corrected model name
from .models import Foto
from .models import Sitio
from .models import Tecnico
from .models import RelatorioFinal  # Corrected model name

admin.site.register(TemplateRelatorio)
admin.site.register(Empresa)
admin.site.register(Administrador)
admin.site.register(Foto)
admin.site.register(Sitio)
admin.site.register(Tecnico)
admin.site.register(RelatorioFinal)
