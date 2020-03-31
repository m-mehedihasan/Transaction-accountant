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

class TransactionList(models.Model):
	provider_name = models.CharField(max_length=100)
	receiver_name = models.CharField(max_length=100)
	amount = models.DecimalField(max_digits=5 ,decimal_places=2)
	paid = models.DecimalField(max_digits=5, decimal_places=2)
	due = models.DecimalField(max_digits=5, decimal_places=2)
	date = models.DateField()
	
	class Meta:
		db_table = "TransactionList"