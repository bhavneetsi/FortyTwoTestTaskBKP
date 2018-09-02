from django.test import TestCase
from t1_contact.models import Contact 



class ContactModelTestCase(TestCase):

	
	def setUp(self):

		self.contact = Contact.objects.create(

			name='Bhavneet',
			surname='Singh',
			dateofdbirth='1983-05-01',
			bio='',
			email='bhavneetsi@gmail.com',
			jabber='bhavneetsi@42cc.co',
			skype='bhavneet.si',
			othercontacts=''
			
		
		)
	
	
	def test_contact_basic(self):

		self.assertEqual(self.contact.name,'Bhavneet')	

