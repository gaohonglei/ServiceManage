from django.shortcuts import render
import xml.etree.ElementTree as ET
import sys,traceback,Ice
#Ice.loadSlice("--underscore /usr/share/openstack-dashboard/openstack_dashboard/dashboards/mydash/overview/perf_util.ice")
Ice.loadSlice("--underscore /root/django/mysite/Server/DeviceWatchService.ice")
import Vistek
def LSDindex(request):
    try:
        communicator=Ice.initialize()
        ServerDetect=Vistek.Device.DeviceWatchServicePrx.checkedCast(communicator.stringToProxy("DeviceWatching:tcp -h 172.16.0.122 -p 50001"))
        if not ServerDetect:
            raise RuntimeError("Invalid proxy")
        physicinfo=ServerDetect.GetPhysicInfo()
#        ServiceStatus=ServerDetect.isDeviceServiceOk()
        for info in physicinfo:
            cpu_Count=info.cpuinfovalue.cpuCount
            cpu_UseRate=info.cpuinfovalue.cpuUseRate
            physic_CpuCount=info.cpuinfovalue.physicCpuCount
            mem_Size=info.meminfovalue.memSize
            use_Mem=info.meminfovalue.useMem
            aviable_MemSize=info.meminfovalue.aviableMemSize
            mem_UseRate=info.meminfovalue.memUseRate
            register_SuccessCount=info.registerinfovalue.registerSuccessCount
            register_FailCount=info.registerinfovalue.registerFailCount
            register_SuccessDeviceList=info.registerinfovalue.registerSucccessDeviceList
            register_FaildDeviceList=info.registerinfovalue.registerFailDeviceList
            service_ID=info.serviceID
            print(service_ID)
        print(dir(physicinfo))
    except:
        traceback.print_exc()
        sys.exit(1)
LSDindex(1)
