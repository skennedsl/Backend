import json
from django.http import HttpResponse
from api.models import Asset, Category, Type, Location
from dispatcher import ViewRequestDispatcher
from geoposition import Geoposition
from api.common.errors import InvalidFieldException

class TypeList(ViewRequestDispatcher):
    def get(self, request):
    	""" List of Asset-Type.

        Endpoint:       /api/asset/type/list/
        HTTP method:    GET
        HTTP headers:   <none>
        Query string:   <none>
        Request body:   <none>

        Response:
        {
            "types": [{
                'id':              Integer
                'name':            String
            }, ...]
        }
        """
        result = {
            'types': [],
        }

        # Get assets from database
        objects = Type.objects.all()

        # Parse assets into result
        for obj in objects:
            # Compile info and append
            asset = {
            	'id': obj.id,
            	'name': obj.name,
            }

            result['types'].append(asset)

        return HttpResponse(self.json_dump(request, result), content_type="application/json")

