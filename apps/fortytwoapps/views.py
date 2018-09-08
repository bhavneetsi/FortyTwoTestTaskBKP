from django.http import HttpResponse
from .models import Contact, Request
from django.views.generic import TemplateView, ListView
from json import dumps
# Create your views here.


class Index(TemplateView):
    template_name = "fortytwoapps/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        return context


class Requests(ListView):
    """
    view to handle request page
    """
    model = Request
    template_name = 'fortytwoapps/requests.html'
    queryset = Request.objects.values()[:10]

    def get(self, request, *args, **kwargs):
        requestlist = Request.objects.values()[:10]
        for request in requestlist:
            request['time'] = request['time'].strftime('%b %d %Y %H:%M:%S')
        if self.request.is_ajax():
            if self.request.GET.get('focus') == 'true':
                Request.objects.filter(viewed=False).update(viewed=True)

            context = {'new_requests': Request.objects.filter(viewed=False)
                       .count(), 'request_list': list(requestlist)}
            return HttpResponse(dumps(context),
                                content_type="application/json")
        return super(Requests, self).get(request, *args, **kwargs)
