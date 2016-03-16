from django.http import HttpResponse
from dispatcher import ViewRequestDispatcher


class ImageUpload(ViewRequestDispatcher):
    def post(self, request):
        response_data = {
            'status': "success",
        }
        return HttpResponse(self.json_dump(request, response_data), content_type="application/json")


class VoiceUpload(ViewRequestDispatcher):
    def post(self, request):
        response_data = {
            'status': "success",
        }
        return HttpResponse(self.json_dump(request, response_data), content_type="application/json")
