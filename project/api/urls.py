from django.conf.urls import include, url
from views.status import Status as ServiceStatus
from views.assets import AssetList, AssetFetch, AssetUpdate, AssetDelete, AssetCreate
from views.media import ImageUpload, VoiceUpload

urlpatterns = [
	url(r'^status/$', ServiceStatus.as_view()),

	url(r'^asset/list/$', AssetList.as_view(), name="assetlist"),
	url(r'^asset/(?P<asset_id>[0-9A-Fa-f]{12})/$', AssetFetch.as_view(), name="asset-list"),
	url(r'^asset/update/(?P<asset_id>[0-9A-Fa-f]{12})/$', AssetFetch.as_view(), name="asset-update"),
	url(r'^asset/delete/(?P<asset_id>[0-9A-Fa-f]{12})/$', AssetDelete.as_view(), name="asset-delete"),
	url(r'^asset/create/$', AssetCreate.as_view(), name="asset-create"),

	url(r'^asset/media/image-upload/(?P<asset_id>[0-9A-Fa-f]{12})/$', ImageUpload.as_view(), name="media-image-upload"),
	url(r'^asset/media/voice-upload/(?P<asset_id>[0-9A-Fa-f]{12})/$', VoiceUpload.as_view(), name="media-voice-upload"),
]
