from django.http import HttpResponse
from dispatcher import ViewRequestDispatcher
from api.models import Asset, MediaImage, MediaVoiceMemo
import sys
from django.core.files.base import ContentFile


class ImageUpload(ViewRequestDispatcher):
    def post(self, request, asset_id):
        asset = Asset.objects.get(id=asset_id)
        response_data = {
            'status': "success"
        }

        try:
            current_media = MediaImage.objects.get(asset=asset)
            current_media.image = request.FILES['image']
            current_media.save()
        except MediaImage.DoesNotExist:
            current_media = MediaImage.objects.create(asset=asset)
            current_media.image = request.FILES['image']
            current_media.save()
        except:
            response_data['status'] = "failed"
        
        return HttpResponse(self.json_dump(request, response_data), content_type="application/json")


class VoiceUpload(ViewRequestDispatcher): 
    def post(self, request, asset_id):
        asset = Asset.objects.get(id=asset_id)
        response_data = {
            'status': "success"
        }

        try:
            current_media = MediaVoiceMemo.objects.get(asset=asset)
            current_media.voice_memo = request.FILES['audio']
            current_media.save()
        except MediaVoiceMemo.DoesNotExist:
            current_media = MediaVoiceMemo.objects.create(asset=asset)
            current_media.voice_memo = request.FILES['audio']
            current_media.save()
        except:
            response_data['status'] = "failed"
        
        return HttpResponse(self.json_dump(request, response_data), content_type="application/json")
