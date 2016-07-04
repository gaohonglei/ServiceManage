from django.shortcuts import render
from .models import ServiceList
# Create your views here.
def index(request):
    service_list=ServiceList.objects.all()
    context={'service_list':service_list}
    return render(request,'ServiceManage/index.html',context)
    
