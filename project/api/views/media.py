import json
from django.http import HttpResponse
from django.views.generic import View
from api.models import Asset, Category, Media, Type, Location
from dispatcher import ViewRequestDispatcher

class ImageUpload(ViewRequestDispatcher):
    def post(self, request):
		response_data = {
		    'status':"success",
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")


class VoiceUpload(ViewRequestDispatcher):
    def post(self, request):
		response_data = {
		    'status':"success",
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")