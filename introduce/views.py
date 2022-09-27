from django.http import HttpResponse
from django.shortcuts import render
from introduce.models import AccessLog


def introduce(request):
    # #case1
    # access_log = AccessLog()
    # access_log.location = 'introduce'
    # access_log.save()

    #case2
    AccessLog.objects.create(
        location='introduce'
    )

    return render(request, 'introduce.html')
