#from django.test import LiveServerTestCase
#from selenium import webdriver

#class ContactTestCase(LiveServerTestCase):
	
#	def setUp(self):
#		self.browser = webdriver.Firefox()
#		self.browser.implicitly_wait(2)


#	def tearDown(self):
#		self.browser.quit()

#	def test_contact_find_lables(self):
#		"""

#		Test for finding contact information on html page

#		"""

		# Create basic django-project that would present your name, surname, date of birth, bio, contacts on the main page.
		# Data should be stored in the DB, that's

    	#manage.py syncdb
    	#manage.py runserver
    	#open the browser and all data are in, loaded from fixtures 
		#home_page = self.browser.get(self.live_server_url + '/')    	
		#start finding lables		
		#brand_element = self.browser.find_element_by_css_selector('.navbar-brand')
		#self.assertEqual('42 Coffee Cups Test Assignment', brand_element.text)
		
		# find all other lables on the page name, surname, date of birth, bio, contacts
		#self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="Name"]'))
		#self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="SurName"]'))
		#self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="DateOfBirth"]'))
		#self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="Bio"]'))
		#self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="Email"]'))
		#self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="Jabber"]'))
		#self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="Skype"]'))
		#self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="OtherContacts"]'))

		#placeholder
		#self.fail('Incomplete Test')
