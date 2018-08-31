from django.shortcuts import render
from django.http import request,HttpResponse
from django.shortcuts import render_to_response

# Create your views here.


def index(request):
	return render_to_response('t1_contact/index.html')