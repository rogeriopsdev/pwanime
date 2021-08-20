from django import forms
from .models import Lancamento

class Lancamentoform(forms.ModelForm):
	class Meta:
		model = Lancamento
		fields ='__all__'