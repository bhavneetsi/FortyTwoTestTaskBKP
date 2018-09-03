from django.db import models

# Create your models here.


class Contact(models.Model):

	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100,blank=True,null=True)
	dateofbirth=models.DateField()
	bio=models.CharField(max_length=500,blank=True,null=True)
	email=models.CharField(max_length=100,blank=True,null=True)
	jabber=models.CharField(max_length=100,blank=True,null=True)
	skype=models.CharField(max_length=100,blank=True,null=True)
	othercontacts=models.CharField(max_length=500,blank=True,null=True)

	