from django.core.urlresolvers import reverse
from fortytwoapps.models import Request


class Requestlog():
    """
    Middleware class to log requests into db

    """

    def process_request(self,request):
        has_viewed=request.path == reverse('requests')
        if not request.is_ajax():
            Request.objects.create(url=request.path,
                                   method=request.method,
                                   viewed=has_viewed)

            