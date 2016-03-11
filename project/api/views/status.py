from django.http import HttpResponse
from django.views.generic import View
import json


class Status(View):
    def get(self, request):
		response_data = {
		    'status':"success",
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
