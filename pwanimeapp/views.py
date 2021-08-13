from django.shortcuts import render

# Create your views here.

def base(request):
	return render(request, "pwanime/base.html")


def index(request):
	return render(request,"pwanime/index.html")



def teste(request):
	return render(request,"pwanime/teste.html")
