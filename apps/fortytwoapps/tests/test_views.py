from django.test import TestCase
from fortytwoapps.models import Contact, Request
from django.core.urlresolvers import reverse
from json import loads


class IndexViewTestCase(TestCase):

    def setUp(self):
        Contact.objects.create(name='Bhavneet1', surname='singh',
                               dateofbirth='1983-05-01',
                               bio='developer',
                               email='bhavneetsi@gmail.com',
                               jabber='bhavneetsi@42cc.co',
                               skype='bhavneet.si',
                               othercontacts='+91946121818')
        self.contact = Contact.objects.first()
        self.url = reverse('index')
        self.response = self.client.get(self.url)

    def test_index_view_render(self):
        """
        basic test for index view to return status 200 as response
        and uses correct template
        """
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'fortytwoapps/index.html')
        self.assertEqual(self.response.context_data['contact'], self.contact)

    def test_index_view_return_contact(self):
        """
        Test to check if index view would return all contact object fields
        """
        fields = ('name', 'surname', 'bio', 'email', 'jabber', 'skype',
                  'othercontacts')

        for field in fields:
            self.assertContains(self.response, getattr(self.contact, field))

        self.assertContains(self.response, 'May 1, 1983')

    def test_index_view_no_data_in_db(self):
        """
        Test index view when there is no data in db
        """
        Contact.objects.all().delete()
        contact = Contact.objects.first()
        self.assertEqual(Contact.objects.count(), 0)
        self.url = reverse('index')
        self.response = self.client.get(self.url)
        self.assertEqual(contact, None)
        self.assertContains(self.response, 'Contact details not in db.')

    def test_more_then_one_record_in_db(self):
        """Test contact view, should return first entry from the DB"""
        self.url = reverse('index')
        self.response = self.client.get(self.url)
        Contact.objects.create(name='Bhavneet1', surname='singh',
                               dateofbirth='1983-05-01')
        contacts = Contact.objects.all()
        self.assertTrue(Contact.objects.count(), 2)
        self.assertEqual(contacts[0], self.response.context_data['contact'])


class TestRequestView(TestCase):

    def setUp(self):
        Request.objects.all().delete()

    def test_max_10_requests_returned(self):
        """Test to check if there are more than 10 request in db only 10 are returned
        """
        for _ in range(11):
            self.client.get('/')
        self.response = self.client.get(reverse('requests'))
        self.assertEqual(len(self.response.context_data['object_list']), 10)

    def test_requests_returned_by_ajax(self):
        """Test the AJAX requests made by browser
        """
        for _ in range(11):
            self.client.get('/')
        self.response = self.client.get('/requests/?focus=true',
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest'
                                        )
        request_list = loads(self.response.content)['request_list']
        self.assertEqual(len(request_list), 10)
        self.assertTrue(all(r.viewed for r in Request.objects.all()))

    def test_not_viewed_requests_by_ajax(self):
    	"""
        Test for checking correct notviewed values returned for ajax requests
        """
        for _ in range(20):
            self.client.get('/')
        self.response = self.client.get('/requests/?focus=false',
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertFalse(all(r.viewed for r in Request.objects.all()))
        new_requests = loads(self.response.content)['new_requests']
        self.assertEqual(new_requests, 20)
