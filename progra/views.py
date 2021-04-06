from django.shortcuts import render, HttpResponse

# Create your views here.
def ent(request):
	return render(request,"inicio.html")