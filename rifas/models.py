from django.db import models


class Comprador(models.Model):
    """
    Comprador das rifas
    """
    nome = models.CharField(verbose_name='nome do comprador', max_length=300)
    cpf = models.CharField(verbose_name='cpf do comprador', max_length=11)
    telefone = models.CharField(verbose_name='Número de celular', max_length=20)
    ref_rifa = models.ForeignKey(verbose_name='Faz referência a qual rifa', to='Rifa', related_name='rifa', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# Create your models here.
class Rifa(models.Model):
    """
    Rifa
    """
    titulo = models.CharField(verbose_name='Título da rifa', max_length=300)
    premio = models.CharField(verbose_name='Descrição do prêmio', max_length=700)
    valor_da_rifa = models.CharField(verbose_name='Valor de cada rifa', max_length=10)
    tamanho_rifa = models.IntegerField(verbose_name='Quantidade de quadrados a sortear')
    fechada = models.BooleanField(verbose_name='Marque para finalizar a rifa', default=False)
    vencedor = models.ForeignKey(verbose_name='Vencedor do prêmio', to=Comprador, on_delete=models.CASCADE, related_name='comprador', null=True, blank=True)
    data_inicio = ... # Ainda irei fazer
    data_termino = ... # Ainda irei fazer

    def __str__(self):
        return self.titulo
    



