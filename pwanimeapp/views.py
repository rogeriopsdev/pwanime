from django.shortcuts import render
from .forms import Lancamentoform
from .models import Lancamento

# Create your views here.

def base(request):
	return render(request, "pwanime/base.html")


def index(request):
	lancamentos = Lancamento.objects.all()
	return render(request,"pwanime/index.html", {'lancamentos':lancamentos})



def criar_lancamento(request):
	form =Lancamentoform(request.POST)
	if request.method =="POST":
		form = Lancamentoform(request.POST, request.FILES)
		if form.is_valid():
			obj =form.save()
			obj.save()
			form =Lancamentoform()

	return render(request,"pwanime/criar_lancamento.html", {'form':form})
