from django.db import models

class Tecnico(models.Model):
    idtecnico = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Sitio(models.Model):
    idsitio = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    CEP = models.CharField(max_length=8)
    cidade = models.CharField(max_length=45)
    endereco = models.CharField(max_length=45)

    def __str__(self):
        return self.nome


class Foto(models.Model):
    idfoto = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='fotos/')
    descricao = models.TextField()
    metadados = models.JSONField()
    idsitio = models.ForeignKey(Sitio, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


class Administrador(models.Model):  # Corrected class name
    idadministrador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    senha = models.CharField(max_length=45)

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    idempresa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome


class TemplateRelatorio(models.Model):  # Corrected class name
    idtemplate_relatorio = models.AutoField(primary_key=True)
    pedidos_fotos = models.JSONField()
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)  # Fixed field name
    idempresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Template {self.idtemplate_relatorio}"  # Changed to avoid missing 'nome'


class RelatorioFinal(models.Model):  # Corrected class name
    idrelatorio_final = models.AutoField(primary_key=True)
    endereco_server = models.CharField(max_length=150)
    tecnico_responsavel = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    idsitio = models.ForeignKey(Sitio, on_delete=models.CASCADE)
    idtemplate_relatorio = models.ForeignKey(TemplateRelatorio, on_delete=models.CASCADE)
    data = models.DateField()
    fotos = models.ManyToManyField(Foto)  # Changed field name to plural
    data_visita = models.DateField()

    def __str__(self):
        return f"Report from {self.data}"
