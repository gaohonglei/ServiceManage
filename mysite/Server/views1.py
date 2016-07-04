from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from horizon import views

import sys,traceback,Ice
Ice.loadSlice("/usr/share/openstack-dashboard/openstack_dashboard/dashboards/mydash/overview/perf_util.ice")
#Ice.loadSlice("/usr/share/openstack-dashboard/openstack_dashboard/dashboards/mydash/overview/DeviceWatchService.ice")
import Vistek

class IndexView(views.HorizonTemplateView):
    template_name= 'mydash/overview/index.html'

#    def __init__(self):
#        self.ResultType=Vistek.Perf.ResponseStringType.rstXml
#        self.communicator=Ice.initialize()
        #self.ServerDetect=Vistek.Perf.ServicePerfPrx.checkedCast(self.communicator.stringToProxy("DeviceServicePerf:tcp -h 172.16.0.20 -p 54321"))
#        if not self.ServerDetect:
 #           raise RuntimeError("Invalid proxy")
 
    def get_context_data(self,**kwargs):
        context=super(IndexView,self).get_context_data(**kwargs)
        try:
            ResultType=Vistek.Perf.ResponseStringType.rstXml
            communicator=Ice.initialize()
            ServerDetect=Vistek.Perf.ServicePerfPrx.checkedCast(communicator.stringToProxy("DeviceServicePerf:tcp -h 172.16.0.20 -p 54321"))
            #ServerDetect=Vistek.Device.DeviceWatchServicePrx.checkedCast(communicator.stringToProxy("DeviceWatching:tcp -h 172.16.0.122 -p 50000"))
            if not ServerDetect:
                raise RuntimeError("Invalid proxy")
            result=ServerDetect.GetSumRate(ResultType)
            #result=ServerDetect.GetServiceRunningInfo()
            client_list=ServerDetect.GetAllClients()
            
	    info=""
            for client in client_list:
                info += str(client.IP)
                info +="   "
                info += str(client.port)
                info += "   "
            
            context['Result']=result
            context['info']=info
            communicator.destroy()
        except:
            traceback.print_exc()

        return context

'''
class IndexView(views.HorizonTemplateView):
    # A very simple class-based view...
    template_name = 'mydash/overview/index.html'
    page_title = _("abc")
    def get_context_data(self,**kwargs):
        # Add data to the context here...
        context=super(IndexView, self).get_context_data(**kwargs)
        context["abc"]="acb"
        return context

class IndexView(views.HorizonTemplateView):
    # A very simple class-based view...
    template_name = 'mydash/overview/index.html'

    page_title = _("abc")
    def get_context_data(self, **kwargs):
        # Add data to the context here...
        context = super(IndexView, self).get_context_data(**kwargs)
 	context["service"]="abc"
        return context


class IndexView(views.APIView):
    # A very simple class-based view...
    template_name = 'mydash/overview/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
'''
