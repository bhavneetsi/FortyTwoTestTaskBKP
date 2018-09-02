from django.shortcuts import render
from django.http import request,HttpResponse
from django.shortcuts import render_to_response
from .models import Contact
# Create your views here.


def index(request):
	context= {'contact': Contact.objects.first()}
	return render_to_response('t1_contact/index.html',context)
