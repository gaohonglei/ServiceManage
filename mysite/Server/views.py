from django.shortcuts import render
from .models import LSDService,GZYMediaService,GZYDeviceService
import xml.etree.ElementTree as ET
import sys,traceback,Ice
Ice.loadSlice("--underscore /root/django/mysite/Server/perf_util.ice")
Ice.loadSlice("--underscore /root/django/mysite/Server/DeviceWatchService.ice")
import Vistek
def LSDice():
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
            LSDService.objects.create(service_id=service_ID,cpuCount=int(cpu_Count),physicCpuCount=int(physic_CpuCount),cpuUseRate=float(cpu_UseRate),memSize=int(mem_Size),useMem=int(use_Mem),aviableMemSize=int(aviable_MemSize),memUseRate=float(mem_UseRate),rigisterSucessCount=int(register_SuccessCount),registerSucessDeviceList=register_SuccessDeviceList,registerFaildCount=int(register_FailCount),registerFailDeviceList=register_FaildDeviceList)
        communicator.destroy()
    except:
        traceback.print_exc()
        sys.exit()


def GZYMedia():
    try:
        ResultType=Vistek.Perf.ResponseStringType.rstXml
        communicator=Ice.initialize()
        ServerMediaDetect=Vistek.Perf.MediaServicePerfPrx.checkedCast(communicator.stringToProxy("MediaServicePerf:tcp -h 172.16.0.80 -p 54333"))

        if not ServerMediaDetect:
            raise RuntimeError("Invalid proxy")
        result=ServerMediaDetect.GetSumRate(ResultType)
        client_list= ServerMediaDetect.GetAllClients()
        pipelines = ServerMediaDetect.GetAllPipelines()
        root=ET.fromstring(result)
        perf=root.getiterator('perf')
        Service_ID=perf[0].attrib['ServiceId']
        Client_Count=perf[0].attrib['ClientCount']
        MaxClient_Count=perf[0].attrib['MaxClientCount']
        Down_Rate=perf[0].attrib['DownRate']
        Up_Rate=perf[0].attrib['UpRate']
        Timestamp_Ticks=perf[0].attrib['TimestampTicks']

        client_info=''
        for client in client_list:
            client_info += client.IP
            client_info +=':'
            client_info += str(client.port)
            client_info += ':'
            client_info += str(client.UpRate)
            client_info += ';'
        Pipeline_info=''
        for pipeline in pipelines:
            Pipeline_info += pipeline.uri
            Pipeline_info += '-'
            Pipeline_info += str(pipeline.DownRate)
            Pipeline_info +=';'
        GZYMediaService.objects.filter(service_id=Service_ID).delete()
        GZYMediaService.objects.create(service_id=Service_ID,ClientCount=int(Client_Count),MaxClientCount = int(MaxClient_Count),UpRate=float(Up_Rate),DownRate=float(Down_Rate),Clients_info=client_info,Pipelines=Pipeline_info)
        communicator.destroy()
    except:
        traceback.print_exc()

def GZYDevice():
    try:
        ResultType=Vistek.Perf.ResponseStringType.rstXml
        communicator=Ice.initialize()
        ServerDetect=Vistek.Perf.DeviceServicePerfPrx.checkedCast(communicator.stringToProxy("DeviceServicePerf:tcp -h 172.16.0.80 -p 54321"))
        #ServerMediaDetect=Vistek.Perf.MediaServicePerfPrx.checkedCast(communicator.stringToProxy("MediaServicePerf:tcp -h 172.16.0.80 -p 54333"))

        if not ServerDetect:
            raise RuntimeError("Invalid proxy")
        result=ServerDetect.GetSumRate(ResultType)
        client_list= ServerDetect.GetAllClients()
     
        root=ET.fromstring(result)
        perf=root.getiterator('perf')
        Service_ID=perf[0].attrib['ServiceId']
        Client_Count=perf[0].attrib['ClientCount']
        CheckDevice_Count=perf[0].attrib['CheckDeviceCount']
        Device_Count=perf[0].attrib['DeviceCount']
        Timestamp_Ticks=perf[0].attrib['TimestampTicks']

        client_info=''
        for client in client_list:
            client_info += client.IP
            client_info +=':'
            client_info += str(client.port)
            client_info += ':'
            client_info += str(client.UpRate)
            client_info += ';'
        GZYDeviceService.objects.filter(service_id=Service_ID).delete()
        GZYDeviceService.objects.create(service_id=Service_ID,ClientCount=int(Client_Count),CheckDeviceCount = int(CheckDevice_Count),DeviceCount=int(Device_Count),Clients_info=client_info)
        communicator.destroy()
    except:
        traceback.print_exc()

def index(request):
#    LSDice()
#    service=LSDService.objects.all()
#    GZYMedia()
#    GZYDevice()
#    Media=GZYMediaService.objects.all()
   # Device=GZYDeviceService.objects.all()
    #context={"LSDobject":service,"GZYMediaObject":Media,"GZYDeviceObject":Device}
    return render(request,'Server/index.html') 
def LSDdetail(request,serviceID):
    LSDice()
    service=LSDService.objects.get(service_id=serviceID)
    context={'service':service}
    return render(request,'Server/LSDdetail.html',context)
def GZYMediadetail(request,serviceID):
    service=GZYMediaService.objects.get(service_id=serviceID)
    context={'service':service}
    return render(request,'Server/GZYMediaDetail.html',context)
def GZYDevicedetail(request,serviceID):
    service=GZYDeviceService.objects.get(service_id=serviceID)
    context={'service':service}
    return render(request,'Server/GZYDeviceDetail.html',context)
def DeviceList(request,serviceID,DeviceType):
    service=LSDService.objects.get(service_id=serviceID)
    if DeviceType == 'faildList':
        DeviceList=service.registerFailDeviceList
    else:
        DeviceList=service.registerSucessDeviceList 
    context={"DeviceList":DeviceList.split(':')}
    return render(request,'Server/DeviceList.html',context)
def ClientList(request,serviceID,Type):
    context={}
    try:
        deviceClient=GZYDeviceService.objects.get(service_id=serviceID)
        context["serviceID"]=serviceID
        if Type=='ClientList':
            context["List"]=deviceClient.Clients_info.split(';')
    except GZYDeviceService.DoesNotExist:
        context["serviceID"]=serviceID
        mediaClient=GZYMediaService.objects.get(service_id=serviceID)    
        if Type=='ClientList':
            context["List"]=mediaClient.Clients_info.split(';')
        else:
            context["List"]=mediaClient.Pipelines.split(';')
    return render(request,'Server/ClientList.html',context)
def GZYindex(request):
    GZYMedia()
    GZYDevice()
    Media=GZYMediaService.objects.all()
    Device=GZYDeviceService.objects.all()
    return render(request,'Server/GZYindex.html')  

def LSDindex(request):
    LSDice()
    service=LSDService.objects.all()
    context={"object":service}
    return render(request,'Server/LSDindex.html',context)
