from django.test import TestCase,RequestFactory

from apps.t1_contact.views import index
from django.db.models.query import QuerySet

class IndexViewTestCase(TestCase):

	def setUp(self):

		self.factory = RequestFactory()



	def test_index_view(self):
		""" basic test for index view to return status 200 as response
		and uses correct template

		"""

		request = self.factory.get('/')
		with self.assertTemplateUsed('t1_contact/index.html'):

			response = index(request)
			self.assertEqual(response.status_code,200)



	def test_index_view_return_contact(self):
		"""
		Test to check if index view would return contact object if available
		"""
		response = self.client.get('/')
		self.assertIs(type(response.context['contact']),QuerySet)
