from django.test import TestCase,RequestFactory

from fortytwoapps.views import Index
from django.db.models.query import QuerySet
from fortytwoapps.models import Contact
from django.core.urlresolvers import reverse

class IndexViewTestCase(TestCase):

	def setUp(self):

		
		contact=Contact.objects.create(name='Bhavneet1',surname='singh',dateofbirth='1983-05-01',bio='developer',
			email='bhavneetsi@gmail.com',jabber='bhavneetsi@42cc.co',skype='bhavneet.si',othercontacts='+91946121818')
		self.contact = Contact.objects.first()
		self.url = reverse('index')
		self.response = self.client.get(self.url)
		

	
	def test_index_view_render(self):
		""" 
		basic test for index view to return status 200 as response
		and uses correct template

		"""
		

		self.assertEqual(self.response.status_code,200)
		self.assertTemplateUsed(self.response, 'fortytwoapps/index.html')
		self.assertEqual(self.response.context_data['contact'], self.contact)


	def test_index_view_return_contact(self):

		"""
		Test to check if index view would return all contact object fields
		"""
		
		
		fields = ('name', 'surname','bio', 'email', 'jabber', 'skype','othercontacts')	
		
		for field in fields:
			
			self.assertContains(self.response, getattr(self.contact, field))

		self.assertContains(self.response,'May 1, 1983')
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
		self.assertContains(self.response,'Contact details not in db.')
		
		
	def test_more_then_one_record_in_db(self):
		"""Test contact view, should return first entry from the DB"""
		self.url = reverse('index')
		self.response = self.client.get(self.url)
		Contact.objects.create(name='Bhavneet1',surname='singh',dateofbirth='1983-05-01')
		contacts=Contact.objects.all()
		self.assertTrue(Contact.objects.count(), 2)
		self.assertEqual(contacts[0], self.response.context_data['contact'])
