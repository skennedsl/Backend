from django.conf.urls import include, url
from views.status import Status as ServiceStatus
from views.assets import List as AssetList

urlpatterns = [
	url(r'^status/$', ServiceStatus.as_view()),

	url(r'^asset/list/$', AssetList.as_view(), name="assetlist"),
	# url(r'^asset/(?P<asset_id>[0-9A-Fa-f]{12})/$', ServiceStatus.as_view(), name="assetlist"),
	# url(r'^asset/delete/(?P<asset_id>[0-9A-Fa-f]{12})/$', ServiceStatus.as_view(), name="assetlist"),
	# url(r'^asset/create/(?P<asset_id>[0-9A-Fa-f]{12})/$', ServiceStatus.as_view(), name="assetlist"),
]
