from django.http import HttpResponse
from dispatcher import ViewRequestDispatcher
from api.models import Asset, Media
import sys
from django.core.files.base import ContentFile


class ImageUpload(ViewRequestDispatcher):
    def post(self, request, asset_id):
        asset = Asset.objects.get(id=asset_id)
        response_data = {
            'status': "success"
        }

        try:
            current_media = Media.objects.get(asset=asset)
            current_media.image = request.FILES['image']
            current_media.save()
        except Media.DoesNotExist:
            current_media = Media.objects.create(asset=asset)
            current_media.image = request.FILES['image']
            current_media.save()
        except:
            response_data['status'] = "failed"
        
        return HttpResponse(self.json_dump(request, response_data), content_type="application/json")


class VoiceUpload(ViewRequestDispatcher): 
    def post(self, request):
        asset = Asset.objects.get(id=asset_id)
        response_data = {
            'status': "success"
        }

        try:
            current_media = Media.objects.get(asset=asset)
            current_media.voice_memo = request.FILES['audio']
            current_media.save()
        except Media.DoesNotExist:
            current_media = Media.objects.create(asset=asset)
            current_media.voice_memo = request.FILES['audio']
            current_media.save()
        except:
            response_data['status'] = "failed"
        
        return HttpResponse(self.json_dump(request, response_data), content_type="application/json")
