from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
def index(request):
    
    return render(request,'pages/index.html')

def login(request):
    
    return render(request,'pages/regisLog.html')

def senddata(request):
    postdata = json.loads(request.body.decode('utf-8'))
    
    # name = postdata['name']
    isSuccess=False
    compt=1
    while compt < 100000:
        compt+=1
    name=postdata['name']
    username=postdata['username']
    email=postdata['email']
    phone=postdata['phone']
    passeword=postdata['password']
    passconf=postdata['passconf']
    print("++++++++++++++++++++",username)
    if username is not None:
        isSuccess=True
    else:
        isSuscess=False
    
    datas = {
        'succes':isSuccess,
        'name':name,
        'username':username,
    }
    return JsonResponse(datas, safe=False)