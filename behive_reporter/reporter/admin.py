from django.contrib import admin
from django.utils.html import format_html
from .models import (
    TemplateRelatorio,
    Empresa,
    Administrador,
    Foto,
    Sitio,
    Tecnico,
    RelatorioFinal
)

@admin.register(TemplateRelatorio)
class TemplateRelatorioAdmin(admin.ModelAdmin):
    list_display = ('idtemplate_relatorio', 'administrador', 'idempresa')
    list_filter = ('administrador', 'idempresa')
    search_fields = ('idtemplate_relatorio',)

admin.site.register(Empresa)

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('idadministrador', 'nome', 'email', 'telefone')
    search_fields = ('nome', 'email')

@admin.register(Sitio)
class SitioAdmin(admin.ModelAdmin):
    list_display = ('idsitio', 'nome', 'cidade', 'endereco')
    search_fields = ('nome',)

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('idtecnico', 'nome', 'email', 'telefone')
    search_fields = ('nome', 'email')

class FotoAdmin(admin.ModelAdmin):
    list_display = ('idfoto', 'descricao', 'mostrar_foto', 'caminho')
    readonly_fields = ('caminho', 'mostrar_foto')
    list_filter = ('idsitio', 'descricao')  # Added filter for descricao
    search_fields = ('descricao',)

    def mostrar_foto(self, obj):
        """Display the photo in the admin list."""
        if obj.foto:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.foto.url)
        return 'Sem foto'  # Display default message if no photo exists

    mostrar_foto.short_description = 'Foto'  # Column title for photo

admin.site.register(Foto, FotoAdmin)

@admin.register(RelatorioFinal)
class RelatorioFinalAdmin(admin.ModelAdmin):
    list_display = ('idrelatorio_final', 'data', 'tecnico_responsavel', 'idsitio')
    list_filter = ('tecnico_responsavel', 'idsitio')
    search_fields = ('data',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "fotos":
            sitio = request.GET.get('idsitio')  # Get the ID of the sitio from the request
            if sitio:
                kwargs["queryset"] = Foto.objects.filter(idsitio=sitio)  # Filter photos by sitio
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # You can add custom filtering here based on request.user or other criteria
        return queryset
