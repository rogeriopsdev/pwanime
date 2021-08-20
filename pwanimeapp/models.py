from django.db import models

# Create your models here.
class Lancamento(models.Model):
	nome_lancamento = models.CharField(max_length=200)
	link_lancamento = models.CharField(max_length=200)

	def __str__(self):
		return self.nome_lancamento

