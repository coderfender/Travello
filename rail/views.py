from django.shortcuts import render
from django.shortcuts import HttpResponse
from Train_m import train_status

# Create your views here.

def home(request):
    return render(request,'train_status.html')

def train(request):
    return render(request,'train_default.html')

def rdet(request):
    if request.method == 'POST':
        res = train_status(request.POST['train_num'])
        # return HttpResponse(train_status(request.POST['train_num']))
        return render(request,'realtime.html',{'res':res})

        # return HttpResponse(t)




