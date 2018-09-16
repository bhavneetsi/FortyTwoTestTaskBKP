from django.test import TestCase
from fortytwoapps.models import Contact, Request
from django.core.urlresolvers import reverse
from json import loads
from PIL import Image
from django.core.files import File
from django.conf import settings

class IndexViewTestCase(TestCase):

    def setUp(self):
        Contact.objects.all().delete()
        imgfile = open("".join([settings.BASE_DIR,"/uploads/photos/img.png"]))
        Contact.objects.create(name='Bhavneet1', surname='singh',
                               dateofbirth='1983-05-01',
                               bio='developer',
                               email='bhavneetsi@gmail.com',
                               jabber='bhavneetsi@42cc.co',
                               skype='bhavneet.si',
                               othercontacts='+91946121818',
                               photo=File(imgfile))
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
        #url = reverse('index')
        response = self.client.get('/')
        self.assertEqual(contact, None)
        self.assertContains(response, 'Contact details not in db.')

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
            self.client.get('/page/')
        self.response = self.client.get(reverse('requests'))
        self.assertEqual(len(self.response.context_data['object_list']), 10)

    def test_requests_returned_by_ajax(self):
        """Test the AJAX requests made by browser
        """
        for _ in range(11):
            self.client.get('/page/')
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
            self.client.get('/page/')
        self.response = self.client.get('/requests/?focus=false',
                                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertFalse(all(r.viewed for r in Request.objects.all()))
        new_requests = loads(self.response.content)['new_requests']
        self.assertEqual(new_requests, 20)

    def test_request_view_render(self):
        """
        basic test for request view to return status 200 as response
        and uses correct template
        """
        self.response = self.client.get('/requests/')
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'fortytwoapps/requests.html')


class TestUpdateContactView(TestCase):

    def setUp(self):
        self.url = reverse('update_contact',kwargs={'pk': 1})
        self.client.login(username='admin', password='admin')
        self.response = self.client.get(self.url)

    def test_update_contact_view_render(self):
        """
        Test to check if view is retrself.assertEqual(response.url,
                         '/accounts/login/?next=/update_profile_page/1/')
        ning success status code and rendringself.assertEqual(response.url,
                         '/accounts/login/?next=/update_profile_page/1/')

        correct template
        """
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,'fortytwoapps/update_contact.html')
    
    def test_update_contact_view_unauthorised(self):
        """
        Test if unauthorised request is redirected to login page 
        """
        self.client.logout()
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code,302)
        self.assertEqual(self.response.url,
                         'http://testserver/accounts/login/?next=/updatecontact/1/')

    def test_for_all_fields_presented_back(self):
        """
        Test to check if all fields from model are made available
        to be updated.
        """
        fields = ('name', 'surname', 'bio', 'email', 'jabber', 'skype',
                  'othercontacts', "dateofbirth", "photo")

        for field in fields:
            self.assertContains(self.response, field)
   
    def test_ajax_update_request(self):
        updatedata={'name':'test',
              'surname':'user',
              'dateofbirth':'1983-05-01',
              'email':'testuser@test.com',
              'skype':'test.user',
              'jabber':'test@42cc.co',
              'othercontacts':'none',
              'bio':'no bio'}
        response=self.client.post(self.url,updatedata,HTTP_X_REQUESTED_WITH = "XMLHttpRequest")
        contact=Contact.objects.first()
        self.assertEqual(response.status_code,200)
        self.assertEqual(contact.name, updatedata['name'])
        self.assertEqual(contact.surname, updatedata['surname'])
        self.assertEqual(contact.dateofbirth.strftime('%Y-%m-%d'), updatedata['dateofbirth'])
        self.assertEqual(contact.email, updatedata['email'])
        self.assertEqual(contact.jabber, updatedata['jabber'])
        self.assertEqual(contact.othercontacts,updatedata['othercontacts'])
        self.assertEqual(contact.bio,updatedata['bio'])

