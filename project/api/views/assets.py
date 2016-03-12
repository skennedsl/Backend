from django.http import HttpResponse
from django.views.generic import View
from api.models import Asset, Category, Media, Type, Location
from dispatcher import ViewRequestDispatcher
import json
import sys


"""
NOTES: 

ViewRequestDispatcher - what all requests inherit from
	It catches all exceptions, formulates an error as defined in common/errors.py
	and then displays a consistant error message

@verify_token - decorates all requests
	It calls out to decorators/verify_token.py to validate the token supplied in 
	the request headers
"""


class List(ViewRequestDispatcher):
	def get(self, request):
		"""Registers a new user.

		Endpoint:           /api/asset/list/
		HTTP method:        GET
		HTTP headers:       <none>
		Query string:       <none> 
		Request body:		<none>

		Response:
		{
			"assets": [{
				'name':				String
				'description':		String
				'category':			String
				'asset-type':		String
				'latitude': 		Double
				'longitude': 		Double
				'media-image-url': 	String
				'media-voice-url': 	String
			}, ...]
		}
		"""
		result = {
			'assets':[],
		}
		
		# Get assets from database
		objects = Asset.objects.all()

		# Parse assets into result
		for obj in objects:
			asset_info = {
				'name': obj.name,
				'description': obj.description,
				'category': obj.category.name,
				'asset-type': obj.asset_type.name,
				'latitude': 0.0,
				'longitude': 0.0,
				'media-image-url': "",
				'media-voice-url': "",
			}

			# Get asset location
			locations = Location.objects.filter(asset=obj)
			if len(locations) > 0:
				asset_info['latitude'] = float(locations[0].position.latitude)
				asset_info['longitude'] = float(locations[0].position.longitude)

			# Get asset media
			medias = Media.objects.filter(asset=obj)
			if len(medias) > 0:
				asset_info['media-image-url'] = medias[0].image.url
				asset_info['media-voice-url'] = medias[0].voice_memo.url

			# Append to result
			result['assets'].append(asset_info)

		print >>sys.stderr, 'Goodbye, cruel world!'

		return HttpResponse(json.dumps(result), content_type="application/json")


class Update(ViewRequestDispatcher):
	def get(self, request, asset_id):
		response_data = {
			'status':"success",
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")

	def delete(self, request, asset_id):
		response_data = {
			'status':"success",
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")

	def post(self, request, asset_id):
		response_data = {
			'status':"success",
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")

