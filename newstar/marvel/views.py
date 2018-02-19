from django.shortcuts import render ,redirect
from django.http  import HttpResponse
from .models import Captain
from .forms import CaptainForm


# Create your views here.
def ironman(request):
 	context ={
 		"avengers" :Captain.objects.all(),


 	}
 	return render(request, "list_view.html", context)
