from django.conf.urls import include, url
from views.status import Status as ServiceStatus

urlpatterns = [
	url(r'^status/$', ServiceStatus.as_view()),
    # url(r'^user/login/register/$', Register.as_view(), name='register'),
    # url(r'^user/login/$', Login.as_view(), name='login'),
    # url(r'^user/login/status/$', Login.as_view(), name='status'),
    # url(r'^user/login/refresh/$', Login.as_view(), name='refresh'),
    # url(r'^arduino/', include('arduino.urls', namespace="arduino")),
]
