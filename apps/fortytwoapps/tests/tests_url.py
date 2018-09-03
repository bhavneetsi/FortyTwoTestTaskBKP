from django.test import TestCase

# Create your tests here.


from django.core.urlresolvers import resolve

from fortytwoapps.views import Index

class IndexUrlTestCase(TestCase):


	def test_root_url_for_index_view(self):
		"""
		test if root of url uses index view

		"""

		root=resolve('/')
		self.assertEqual(root.view_name,'index')
