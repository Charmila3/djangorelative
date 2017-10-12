from django.conf.urls import url
from firstapp import views


app_name = 'firstapp'

urlpatterns = [
    url(r'^one/$', views.one, name ="one"),
    url(r'^other/$', views.other, name ="other"),
    url(r'^relative/$', views.relative, name ="relative"),
]