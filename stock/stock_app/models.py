from __future__ import unicode_literals

import uuid
import datetime

from django.db import models
from django.utils.translation import pgettext_lazy
from django.conf import settings


# Create your models here.
class User(models.Model):
	id = models.CharField(max_length=255, default=uuid.uuid4, primary_key=True)
	email = models.CharField(pgettext_lazy('User field', 'email'), null=True, max_length=255, unique=True)
	is_active = models.NullBooleanField(
	    verbose_name=pgettext_lazy('User field', 'Validated'),default=True)
	phone = models.CharField(pgettext_lazy('Phone Field', 'Phone Number/Email'),max_length=15,null = True, unique=True, blank=True)
	first_name = models.CharField(max_length=255, default=uuid.uuid4,
	    		verbose_name=pgettext_lazy('User field', 'Validated'),blank = True)
	middle_name = models.CharField(max_length=255, default=uuid.uuid4,
	    		verbose_name=pgettext_lazy('User field', 'Validated'),blank = True)
	last_name = models.CharField(max_length=255, default=uuid.uuid4,
	    		verbose_name=pgettext_lazy('User field', 'Validated'),blank = True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.first_name)


class Order(models.Model):
	CHOICES = (
	    ('sell', pgettext_lazy('Sell stock', 'sell')),
	    ('buy', pgettext_lazy('Buy Stock', 'Buy'))
	)

	id = models.CharField(max_length=255, default=uuid.uuid4, primary_key=True)
	user = models.ForeignKey(User, related_name="buy_stock", blank=True, null=True)
	type = models.CharField(pgettext_lazy('Stock Buy', 'Stock Buy'), max_length=255, choices=CHOICES)
	amount = models.CharField(pgettext_lazy('Stock Buy', 'Stock Buy'), max_length=255)
	is_done = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id)


class StockAllocation(models.Model):
	id = models.CharField(max_length=255, default=uuid.uuid4, primary_key=True)
	buy_stock = models.ForeignKey(Order, related_name="buy_stock_allocation")
	sell_stock = models.ForeignKey(Order, related_name="sell_stock_allocation")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id)




