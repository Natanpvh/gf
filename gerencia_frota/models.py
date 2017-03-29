from django.db import models

# Cria Model Tipo de Veiculos.
class TipoVeiculo(models.Model):
    tipo = models.CharField(max_length=150)
    cor = models.CharField(max_length=150)
    placa = models.CharField(max_length=9)
    marca = models.OneToOneField("MarcaVeiculo")

    def __str__(self):
        return self.tipo

# Cria model marca do veiculo
class MarcaVeiculo(models.Model):
    marca = models.CharField(max_length=150)

    def __str__(self):
        return self.marca

#Cria a ForeignKey do tipo d maca de Veiculos
class TipoMarca(models.Model):
    id_tipo = models.ForeignKey(TipoVeiculo, verbose_name='TipoVeiculo')
    id_marca = models.ForeignKey(MarcaVeiculo, verbose_name='MarcaVeiculo')