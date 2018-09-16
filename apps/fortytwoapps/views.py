from django.http import HttpResponse
from .models import Contact, Request
from django.views.generic import TemplateView, ListView, UpdateView
import json
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from fortytwoapps.forms import UpdateContactForm
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
            return HttpResponse(json.dumps(context),
                                content_type="application/json")
        return super(Requests, self).get(request, *args, **kwargs)


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)


    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response
    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response


class UpdateContact(AjaxableResponseMixin,UpdateView):
    """View to serve updatecontact 
    """
    model = Contact
    template_name = "fortytwoapps/update_contact.html"
    form_class = UpdateContactForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateView, self).dispatch(*args, **kwargs)
