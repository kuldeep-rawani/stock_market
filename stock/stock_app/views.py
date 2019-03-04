from django.shortcuts import render

# Create your views here.
from .utils import Utils
from .basecontroller import BaseController
from transformer import MatchedUnmatchedList
from .models import User, Order, StockAllocation
from django.views.decorators.csrf import csrf_exempt


def matched_unmatched_list(request):
	basecontroller = BaseController()
	if request.method == 'GET':
		orders = Order.objects.all()
		utils = Utils()
		result, pagination_info = utils.custom_pagination(request, orders)
		return basecontroller.respond_with_paginated_collection(200, result, pagination_info, MatchedUnmatchedList)
	return basecontroller.respond_with_error(404, 'method not found')
	

@csrf_exempt
def take_order(request):
	basecontroller = BaseController()
	if request.method == 'POST':
		data = request.POST
		_type = data['requestType']
		amount = data['amount']
		user_id = data['userId']
		order = Order.objects.create(type=_type, amount=amount, user_id=user)
		return basecontroller.respond_with_success(200, 'Order has been placed')
	return basecontroller.respond_with_error(404, 'method not found')

def allocate_stock(request):
	pass