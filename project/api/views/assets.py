import json
from django.http import HttpResponse
from django.views.generic import View
from api.models import Asset, Category, Media, Type, Location
from dispatcher import ViewRequestDispatcher
from geoposition import Geoposition
from api.common.errors import InvalidFieldException


"""
NOTES: 

ViewRequestDispatcher - what all requests inherit from
	It catches all exceptions, formulates an error as defined in common/errors.py
	and then displays a consistant error message

@verify_token - decorates all requests
	It calls out to decorators/verify_token.py to validate the token supplied in 
	the request headers
"""


def assemble_asset_info(asset_obj):
	result = {
		'id': asset_obj.id,
		'name': asset_obj.name,
		'description': asset_obj.description,
		'category': asset_obj.category.name,
		'asset-type': asset_obj.asset_type.name,
		'latitude': 0.0,
		'longitude': 0.0,
		'media-image-url': "",
		'media-voice-url': "",
	}

	# Get asset location
	locations = Location.objects.filter(asset=asset_obj)
	if len(locations) > 0:
		result['latitude'] = float(locations[0].position.latitude)
		result['longitude'] = float(locations[0].position.longitude)

	# Get asset media
	medias = Media.objects.filter(asset=asset_obj)
	if len(medias) > 0:
		result['media-image-url'] = medias[0].image.url
		result['media-voice-url'] = medias[0].voice_memo.url

	return result


class AssetList(ViewRequestDispatcher):
	def get(self, request):
		"""Fetch list of assets.

		Endpoint:           /api/asset/list/
		HTTP method:        GET
		HTTP headers:       <none>
		Query string:       <none> 
		Request body:		<none>

		Response:
		{
			"assets": [{
				'id':				Integer
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
			# Compile info and append
			result['assets'].append(assemble_asset_info(obj))

		return HttpResponse(self.json_dump(request, result), content_type="application/json")


class AssetFetch(ViewRequestDispatcher):
	def get(self, request, asset_id):
		"""Fetch asset information.

		Endpoint:           /api/asset/<asset_id>/
		HTTP method:        GET
		HTTP headers:       <none>
		Query string:       <none> 
		Request body:		<none>

		Response:
		{
			'id': 				Integer
			'name':				String
			'description':		String
			'category':			String
			'asset-type':		String
			'latitude': 		Double
			'longitude': 		Double
			'media-image-url': 	String
			'media-voice-url': 	String
		}
		"""
		# Fetch asset object
		asset_obj = Asset.objects.get(id=asset_id)

		# Compile asset info
		result = assemble_asset_info(asset_obj)

		return HttpResponse(self.json_dump(request, result), content_type="application/json")


class AssetDelete(ViewRequestDispatcher):
	def delete(self, request, asset_id):
		"""Delete an asset.

		Endpoint:           /api/asset/delete/<asset_id>/
		HTTP method:        DELETE
		HTTP headers:       <none>
		Query string:       <none> 
		Request body:		<none>

		Response:
		{
			'success': Boolean
		}
		"""
		
		num_deleted = Asset.objects.get(id=asset_id).delete()

		result = {'success':False}

		if num_deleted > 0:
			result['success'] = True

		return HttpResponse(self.json_dump(request, result), content_type="application/json")


class AssetUpdate(ViewRequestDispatcher):
	def put(self, request, asset_id):
		"""Update an asset

		Endpoint:           /api/asset/update/<asset_id>/
		HTTP method:        PUT
		HTTP headers:       <none>
		Query string:       <none> 

		# all fields must be present
		Request body:		{
			'name':					String
			'description':			String
			'category-name':		String  # If category doesnt exist, it will be created
			'category-description':	String 
			'type-name':			string  # If type doesnt exist, it will be created
			'latitude': 			Double
			'longitude': 			Double
		}

		Response:
		{
			'success': Boolean
		}
		"""

		asset_obj = Asset.objects.get(id=asset_id)

		data = json.loads(request.body)
		try:
			name = data['name']
			description = data['description']
			categ = data['category']
			categ_description = data['categ_description']
			asset_t = data['asset-type']
			latitude = data['latitude']
			longitude = data['longitude']
		except KeyError: 
			raise InvalidFieldException('Body not formatted correctly')

		asset_obj.name = name
		asset_obj.description = description

		# Update Position
		try:
			asset_location = Location.objects.get(asset=asset_obj)
			asset_location.position.longitude = longitude
			asset_location.position.latitude = latitude
			asset_location.save()
		except Location.DoesNotExist:
			new_location = Location.objects.create(position=Geoposition(latitude,longitude), asset=asset_obj)		
			new_location.save()

		# Update Category
		if asset_obj.category.name == categ:
			asset_obj.category.description = categ_description
		else:
			try: 
				# If exists, replace and update
				new_categ = Category.objects.get(name=categ)
				new_categ.description = categ_description
				new_categ.save()
				asset_obj.category = new_categ
			except Category.DoesNotExist:
				# If D.N.E, create and replace
				new_categ = Category.objects.get(name=categ, description=categ_description)
				new_categ.save()
				asset_obj.category = new_categ

		# Update AssetType
		if not asset_obj.asset_type.name == asset_t:
			try: 
				# If exists, update and replace
				new_type = Type.objects.get(name=asset_t)
				new_type.save()
				asset_obj.asset_type = new_type
			except Type.DoesNotExist:
				# If D.N.E, create and replace
				new_type = Type.objects.get(name=asset_t)
				new_type.save()
				asset_obj.asset_type = new_type

		asset_obj.save()

		return HttpResponse(self.json_dump(request, {'success':True}), content_type="application/json")


class AssetCreate(ViewRequestDispatcher):
	def post(self, request, asset_id):
		"""Create an asset

		Endpoint:           /api/asset/create/<asset_id>/
		HTTP method:        POST
		HTTP headers:       <none>
		Query string:       <none> 

		# all fields must be present
		Request body:		{
			'name':					String
			'description':			String
			'category-name':		String  # If category doesnt exist, it will be created
			'category-description':	String 
			'type-name':			string  # If type doesnt exist, it will be created
			'latitude': 			Double
			'longitude': 			Double
		}

		Response:
		{
			'success': Boolean
		}
		"""

		# Raise exception if asset exists
		if len(Asset.objects.filter(id=asset_id)) > 0:
			raise InvalidFieldException('Asset already exists')

		try:
			data = json.loads(request.body)
			name = data['name']
			description = data['description']
			categ = data['category']
			categ_description = data['categ_description']
			asset_t = data['asset-type']
			latitude = data['latitude']
			longitude = data['longitude']
		except KeyError:
			raise InvalidFieldException('Body not formatted correctly')

		new_asset = Asset.objects.create(name=name)

		# Add Name & Description
		new_asset.name = name
		new_asset.description = description

		# Add Possition
		new_location = Location.objects.create(position=Geoposition(latitude,longitude), asset=new_asset)		
		new_location.save()

		# AssetCategory
		try: 
			# If exists, replace and update
			new_categ = Category.objects.get(name=categ)
			new_categ.description = categ_description
			new_categ.save()
			new_asset.category = new_categ
		except Category.DoesNotExist:
			# If D.N.E, create and replace
			new_categ = Category.objects.get(name=categ, description=categ_description)
			new_categ.save()
			new_asset.category = new_categ

		# AssetType
		try: 
			# If exists, update and replace
			new_type = Type.objects.get(name=asset_t)
			new_type.save()
			new_asset.asset_type = new_type
		except Type.DoesNotExist:
			# If D.N.E, create and replace
			new_type = Type.objects.get(name=asset_t)
			new_type.save()
			new_asset.asset_type = new_type

		return HttpResponse(self.json_dump(request, {'success':True}), content_type="application/json")

