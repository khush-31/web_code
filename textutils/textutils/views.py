from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def removepunc(request):
    pass
    # print(request.GET.get('text'))
    # return HttpResponse("removed")
