from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    tempo_servico = models.IntegerField(help_text="Tempo de serviço em anos")
    remuneracao = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
