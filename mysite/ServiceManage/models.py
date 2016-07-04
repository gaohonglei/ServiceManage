from __future__ import unicode_literals

from django.db import models

class ServiceList(models.Model):
    service_id = models.CharField(max_length=20)
    registed_date = models.DateTimeField('date registed')
    service_ip = models.CharField(max_length=20)
    service_owner = models.CharField(max_length=20,default="vistek")
    service_port = models.IntegerField()
    proxy_string= models.CharField(max_length =100)
    service_status=models.CharField(max_length=5,default="false")
    def __str__(self):
        return self.service_id
