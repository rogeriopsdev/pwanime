from django.db import models

# Create your models here.
class Lancamento(models.Model):
	nome_lancamento = models.CharField(max_length=200)
	link_lancamento = models.CharField(max_length=200)

		
	def video_url(self):
		if self.link_lancamento and hasattr(self.link_lancamento, 'url'):
			return self.link_lancamento
		else:
			return self.nome_lancamento



	def __str__(self):
		return self.nome_lancamento



