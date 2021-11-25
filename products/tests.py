from django.test import TestCase
from .models import *

class ProductsModelTests(TestCase):
	def porducts_name(self):
		new_product = Job(name='Cheese Pizza')
		print(new_job)
		self.assertIs(str(new_job), 'Cheese Pizza')