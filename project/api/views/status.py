from django.http import HttpResponse
from django.views.generic import View
import json


class Status(View):
    def get(self, request):
		"""Registers a new user.

		Endpoint:           /companion/user/register/
		HTTP method:        POST
		HTTP headers:       <none>
		Query string:       <none> 

		Response:
		{
			"status": string
		}
		"""
		response_data = {
		    'status':"success",
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
