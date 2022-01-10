from django.db import models


# Create your models here.
class pc(models.Model):
    ip = models.CharField(max_length=30)
    time = models.DateTimeField()
    cpu_num = models.CharField(max_length=5)
    cpu_percent = models.CharField(max_length=30)
    memory_total = models.CharField(max_length=30)
    memory_ava = models.CharField(max_length=30)
    memory_per = models.CharField(max_length=30)
    disk_total = models.CharField(max_length=30)
    disk_free = models.CharField(max_length=30)
    net_sent = models.CharField(max_length=30)
    net_rec = models.CharField(max_length=30)
