from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^LSDService/$',views.LSDindex,name ='LSDService'),
    url(r'^GZYService/$', views.GZYindex, name='GZYService'),
    url(r'^LSDService/([^/]+)/$',views.LSDdetail,name='LSDdetail'),
    url(r'^GZYMediaService/([^/]+)/$',views.GZYMediadetail,name='GZYMediadetail'),
    url(r'^GZYDeviceService/([^/]+)/$',views.GZYDevicedetail,name='GZYDevicedetail'),
    url(r'^GZYDeviceService/([^/]+)/([^/]+)/$',views.ClientList,name='DeviceClientList'),
    url(r'^GZYMediaService/([^/]+)/([^/]+)/$',views.ClientList,name='MediaClientList'),
    
    url(r'^LSDService/([^/]+)/([^/]+)/$',views.DeviceList,name='DeviceList'),
]
