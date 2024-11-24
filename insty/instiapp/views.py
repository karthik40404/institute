from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.
def homi(req):
    return render(req,'index.html')

def admhom(req):
    return render(req,'admin/home.html')

def log(req):
    if 'shop' in req.session:
        return redirect (admhom)
    if req.method=='POST':
        uname=req.POST['uname']
        psw=req.POST['psw']
        data=authenticate(username=uname,password=psw)
        print(data)
        return redirect(log)
    return render(req,'login.html')

def addcourse(req):
    if 'admin' in req.session:
        if req.method=='POST':
            cid=req.POST['cid']
            cname=req.POST['cname']
            disc=req.POST['disc']
            price=req.POST['price']
            file=req.FILES['img']
            data=Course.objects.create(cid=cid,cname=cname,disc=disc,price=price,img=file)
            data.save()
            return redirect(admhom)
        else:
            return render(req,'admin/addc.html')
    else:
        return redirect(log)
