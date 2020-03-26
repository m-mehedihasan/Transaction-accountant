from django.db import models

class Users(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=30)
	confirm_password = models.CharField(max_length=30)
	contact_no = models.CharField(max_length=20)
	
	class Meta:
		db_table = "Users"