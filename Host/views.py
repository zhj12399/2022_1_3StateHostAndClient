from django.http import HttpResponse
from django.db import models
from django.shortcuts import render
import datetime
from .models import pc


# Create your views here.

def getMessage(request):
    if request.method == "POST":
        ip = ""
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META.get("HTTP_X_FORWARDED_FOR")
        else:
            ip = request.META.get("REMOTE_ADDR")
        cpu_num = request.POST.get("cpu_num")
        cpu_percent = request.POST.get("cpu_percent")
        memory_total = request.POST.get("memory_total")
        memory_ava = request.POST.get("memory_ava")
        memory_per = request.POST.get("memory_per")
        disk_total = request.POST.get("disk_total")
        disk_free = request.POST.get("disk_free")
        net_sent = request.POST.get("net_sent")
        net_rec = request.POST.get("net_rec")
        time = request.POST.get("time")

        try:
            pc.objects.get(ip=ip)
        except:
            pc.objects.create(ip=ip, time=time, cpu_num=cpu_num, cpu_percent=cpu_percent, memory_total=memory_total,
                              memory_ava=memory_ava, memory_per=memory_per, disk_total=disk_total,
                              disk_free=disk_free,
                              net_sent=net_sent, net_rec=net_rec)
        else:
            pc.objects.filter(ip=ip).update(cpu_num=cpu_num, time=time, cpu_percent=cpu_percent,
                                            memory_total=memory_total,
                                            memory_ava=memory_ava, memory_per=memory_per, disk_total=disk_total,
                                            disk_free=disk_free,
                                            net_sent=net_sent, net_rec=net_rec)

        return HttpResponse("ok")


def home(request):
    pcs = pc.objects.all()

    text = ""
    num = 1

    for p in pcs:
        p.time = p.time + datetime.timedelta(hours=8)

        text += str(
            num) + " " + p.time.strftime(
            "%m-%d %H:%M:%S") + ' - ' + p.ip + ' - ' + p.cpu_num + ' - ' + p.cpu_percent + ' - ' + p.memory_total + ' - ' + p.memory_ava \
                + ' - ' + p.memory_per + ' - ' + p.disk_total + ' - ' + p.disk_free + ' - ' + p.net_sent + ' - ' + p.net_rec + " <br> "
        num += 1
    return render(request, "home.html", {"text": text})
