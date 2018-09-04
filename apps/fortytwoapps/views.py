from django.shortcuts import render
from django.http import request,HttpResponse
from django.shortcuts import render_to_response
from .models import Contact
from django.views.generic import TemplateView,ListView
# Create your views here.


class Index(TemplateView):
    template_name="fortytwoapps/index.html"

    def get_context_data(self,**kwargs):
        context=super(Index,self).get_context_data(**kwargs)
        context['contact']=Contact.objects.first()
        return context


class Requests(ListView):
    """
    view to handle request page

    """
    pass

        