from django.conf.urls import include, url
from views.home import Home

urlpatterns = [
    url(r'^$', Home.as_view(), name='index'),
    # url(r'^user/login/$', Login.as_view(), name='login'),
    # url(r'^user/login/status/$', Login.as_view(), name='status'),
    # url(r'^user/login/refresh/$', Login.as_view(), name='refresh'),
    # url(r'^status/$', ServiceStatus.as_view()),
    # url(r'^arduino/', include('arduino.urls', namespace="arduino")),
]
