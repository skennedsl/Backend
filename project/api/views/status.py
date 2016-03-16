from django.http import HttpResponse
from dispatcher import ViewRequestDispatcher


class Status(ViewRequestDispatcher):
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
            'status': "success",
        }
        return HttpResponse(self.json_dump(request, response_data), content_type="application/json")
