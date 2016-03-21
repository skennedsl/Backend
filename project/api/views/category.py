import json
from django.http import HttpResponse
from api.models import Asset, Category, Type, Location
from dispatcher import ViewRequestDispatcher
from geoposition import Geoposition
from api.common.errors import InvalidFieldException

class CategoryList(ViewRequestDispatcher):
    def get(self, request):
    	""" List of Asset-Category.

        Endpoint:       /api/asset/category/list/
        HTTP method:    GET
        HTTP headers:   <none>
        Query string:   <none>
        Request body:   <none>

        Response:
        {
            "categories": [{
                'id':              Integer
                'name':            String
                'description':     String
            }, ...]
        }
        """
        result = {
            'categories': [],
        }

        # Get assets from database
        objects = Category.objects.all()

        # Parse assets into result
        for obj in objects:
            # Compile info and append
            category = {
            	'id': obj.id,
            	'name': obj.name,
                'description': obj.description,
            }

            result['categories'].append(category)

        return HttpResponse(self.json_dump(request, result), content_type="application/json")

