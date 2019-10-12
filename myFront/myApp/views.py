from django.shortcuts import render
from django.http import JsonResponse
import json
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import  authenticate ,login ,logout
from .models import *
# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def login(request):
    return render(request,'pages/regisLog.html')

def register(request):
    return render(request,'pages/resgiterImage.html')

def senddata(request):
    postdata = json.loads(request.body.decode('utf-8'))
    
    # name = request.POST['name']
    isSuccess=False
    compt=1
    while compt < 10000000:
        compt+=1
    name=postdata['name']
    username=postdata['username']
    email=postdata['email']
    phone=postdata['phone']
    password=postdata['password']
    passconf=postdata['passconf']
    print("++++++++++++++++++++",username)
    emailOk=False
    print("Name +++++++++++++++++++",name)
    print("Name +++++++++++++++++++",username)
    print("Name +++++++++++++++++++",phone)
    if ((name is not None) and (username is not None) and (phone is not None) ):
        try:
            validate_email(email)
            emailOk=True
        except:
            result={
                'success':False,
                'message':'Email is not valide'
            }
        if emailOk:
            try:
                user = Customer(username =username, name = name, email = email,phone=phone,password=password)
                user.save()
                result={
                    'success':True,
                    'message':'Enregistrement Effectue avec success '
                }
            except Exception as err:
                print(err)
                result={
                    'success':False,
                    'message':'Error lor de l\'enregistrement '
                }
    else:
        result={
            'success':False,
            'message':'Veille verifier tous vos champs'
        }

    return JsonResponse(result, safe=False)

def postsImage(request):
    # postdata = json.loads(request.body.decode('utf-8'))
        
    # name = request.POST['name']
    isSuccess=False
    compt=1
    while compt < 1000000:
        compt+=1
    if request.POST is not None:
        
        name=request.POST.get('name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        passconf=request.POST.get('passconf')
        print("Name ++++++++++++++++++++",name)
        print("Username ++++++++++++++++++++",username)
        print("Phone ++++++++++++++++++++",phone)
        emailOk=False
        if ((name is not None) and (username is not None) and (phone is not None) ):
            image=request.FILES['file']
            try:
                validate_email(email)
                emailOk=True
            except:
                result={
                    'success':False,
                    'message':'Email is not valide'
                }
            if emailOk:
                try:
                    user = Customer(username =username, name = name, email = email,phone=phone,image=image,password=password)
                    user.save()
                    
                    result={
                        'success':True,
                        'message':'Enregistrement Effectue avec success '
                    }
                except Exception as err:
                    print(err)
                    result={
                        'success':False,
                        'message':'Error lor de l\'enregistrement '
                    }
        else:
            result={
                'success':False,
                'message':'Veille verifier tous vos champs'
            }
    else:
        result={
            'success':False,
            'message':'Empty form '
        }
    
  
    print("+++++++++++++++++++++++++++++\n",request.POST['username'])
    print("+++++++++++++++++++++++++++++\n",request.FILES['file'])

    return JsonResponse(result, safe=False)

    