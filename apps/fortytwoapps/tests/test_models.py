from django.test import TestCase
from fortytwoapps.models import Contact, Request
from datetime import date
from factory import fuzzy


class ContactModelTestCase(TestCase):
    """Test for Model datatype
    """
    def setUp(self):
        self.contact = Contact.objects.create(
            name='Bhavneet',
            surname='Singh',
            dateofbirth='1983-05-01',
            bio='',
            email='bhavneetsi@gmail.com',
            jabber='bhavneetsi@42cc.co',
            skype='bhavneet.si',
            othercontacts=''
        )

    def test_contact_basic(self):
        """
        Test for Contact model
        """
        self.assertEqual(self.contact.name, 'Bhavneet')


class RequestsModelTestCase(TestCase):
    """Test for RequestModel
    """
    def setUp(self):
            Request.objects.create(
                                   url='/',
                                   method='get',
                                   time=fuzzy.FuzzyDate(date.today()),
                                   viewed=False)

    def test_request_basic(self):
        """
        Test for Request model
        """
        self.request = Request.objects.first()
        self.assertEqual(self.request.url, '/')
        self.assertEqual(self.request.method, 'get')
        self.assertEqual(self.request.viewed, False)
