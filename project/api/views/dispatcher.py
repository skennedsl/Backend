import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from api.common.errors import ApplicationException, GeneralException


class ViewRequestDispatcher(View):
    """A base class which serves two purposes:
     1. Handle dispatching to a specific handle_XXX method for each request type
     2. Catch and gracefully handle all exceptions"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        try:
            return super(ViewRequestDispatcher, self).dispatch(request, *args, **kwargs)

        except ApplicationException as ae:
            return self.handle_exception(ae, request)

        # except Exception as e:
        #    return self.handle_exception(GeneralException(e), request)

    def handle_exception(self, e, request):

        result = {
            'code': e.code,
            'message': e.msg
        }

        response = HttpResponse(self.json_dump(request, result), content_type='application/json')
        response.status_code = e.status_code

        return response

    @staticmethod
    def json_dump(request, object):
        try:
            pretty = request.GET['prettyPrint']
        except KeyError:
            pretty = 'false'

        if pretty and pretty.lower() == 'true' or pretty == '1':
            return json.dumps(object, indent=4, sort_keys=True)
        else:
            return json.dumps(object)
