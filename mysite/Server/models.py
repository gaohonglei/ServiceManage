from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LSDService(models.Model):
    service_id = models.CharField(max_length=20)
#    status = models.BooleanField()
#    error_msg= models.CharField(max_length=50)
    cpuUseRate = models.DecimalField(max_digits=10,decimal_places=2)
    cpuCount = models.IntegerField()
    physicCpuCount = models.IntegerField()
    memSize= models.IntegerField()
    useMem= models.IntegerField()
    aviableMemSize = models.DecimalField(max_digits=10,decimal_places=2)
    memUseRate = models.DecimalField(max_digits=3,decimal_places=2)
    rigisterSucessCount = models.IntegerField()
    registerFaildCount = models.IntegerField()
    registerSucessDeviceList = models.CharField(max_length=1000)
    registerFailDeviceList= models.CharField(max_length = 1000)
    def __str__(self):
        return self.service_id
class GZYDeviceService(models.Model):
    service_id = models.CharField(max_length=20,default = "abc")
    ClientCount = models.IntegerField()
    CheckDeviceCount = models.IntegerField()
    DeviceCount = models.IntegerField()
    Clients_info = models.CharField(max_length=10000)
    def __str__(self):
        return self.service_id
class GZYMediaService(models.Model):
    service_id = models.CharField(max_length=20,default = "abc")
    ClientCount = models.IntegerField()
    MaxClientCount = models.IntegerField()
    UpRate = models.DecimalField(max_digits=10,decimal_places=2)
    DownRate = models.DecimalField(max_digits=10,decimal_places=2)
    Clients_info = models.CharField(max_length=10000)
    Pipelines= models.CharField(max_length=10000)
    def __str__(self):
        return self.service_id
