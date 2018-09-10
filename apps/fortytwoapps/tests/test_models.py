from django.test import TestCase
from fortytwoapps.models import Contact, Request
from datetime import date
from factory import fuzzy
from PIL import Image
from django.core.files import File
from django.conf import settings

class ContactModelTestCase(TestCase):
    """Test for Model datatype
    """
    def setUp(self):
        Contact.objects.all().delete()
        imgfile = open("".join([settings.BASE_DIR,"/uploads/photos/img.png"]))
        Contact.objects.create(
                               name='Bhavneet',
                               surname='Singh',
                               dateofbirth='1983-05-01',
                               bio='Bio of bhavneet',
                               email='bhavneetsi@gmail.com',
                               jabber='bhavneetsi@42cc.co',
                               skype='bhavneet.si',
                               othercontacts='+919461218818',
                               photo=File(imgfile)
        )
        self.contact = Contact.objects.first()

    def test_contact_basic(self):
        """
        Test for Contact model
        """
        
        self.assertEqual(self.contact.name, 'Bhavneet')
        self.assertEqual(self.contact.surname,'Singh')
        self.assertEqual(self.contact.dateofbirth,date(1983, 5, 1))
        self.assertEqual(self.contact.bio,'Bio of bhavneet')
        self.assertEqual(self.contact.email,'bhavneetsi@gmail.com')
        self.assertEqual(self.contact.jabber,'bhavneetsi@42cc.co')
        self.assertEqual(self.contact.skype,'bhavneet.si')
        self.assertEqual(self.contact.photo.url,'/uploads/photos/img.jpg')

    def test_image_size(self):
        """
        Test if size of stored image is as per size requirements of 200*200
        """
        required_photo_size=(200,200)
        uploaded_photo_size = Image.open(self.contact.photo.path).size
        self.assertEqual(required_photo_size,uploaded_photo_size)

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
